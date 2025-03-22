import os
import sqlite3
from datetime import datetime
import platform
import simpleaudio as sa

# 数据库路径
DB_PATH = os.path.expanduser("~/.flowtimer.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            duration INTEGER,
            mode TEXT
        )
    """)
    conn.close()

def save_record(duration, mode):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # 显式插入时间戳（避免默认值时区问题）
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO sessions (start_time, duration, mode) VALUES (?, ?, ?)",
            (timestamp, duration, mode)
        )
        conn.commit()  # 确保提交事务
        # conn.close()
    except Exception as e:
        print(f"[ERROR] 保存记录失败: {e}")
    finally:
        if conn:
            conn.close()  # 确保连接关闭

def send_notification(message):
    system = platform.system()
    if system == "Darwin":
        os.system(f"osascript -e 'display notification \"{message}\"'")
    elif system == "Linux":
        os.system(f'notify-send "FlowTimer" "{message}"')
    elif system == "Windows":
        from win10toast import ToastNotifier
        ToastNotifier().show_toast("FlowTimer", message)

def play_sound(sound_path):
    try:
        wave_obj = sa.WaveObject.from_wave_file(sound_path)
        wave_obj.play()
    except Exception as e:
        print(f"播放失败: {e}")

def get_daily_stats():
    conn = sqlite3.connect(DB_PATH)
    # 使用本地日期计算（避免 SQLite 内置 DATE() 的时区问题）
    today_start = datetime.now().strftime("%Y-%m-%d 00:00:00")
    today_end = datetime.now().strftime("%Y-%m-%d 23:59:59")
    
    cursor = conn.execute("""
        SELECT SUM(duration), COUNT(*) 
        FROM sessions 
        WHERE start_time BETWEEN ? AND ?
          AND mode = 'work'
    """, (today_start, today_end))
    
    total, count = cursor.fetchone() or (0, 0)
    return total or 0, count or 0

def get_daily_stats_2():
    conn = sqlite3.connect(DB_PATH)
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # 查询当日所有记录（忽略具体时间）
    cursor = conn.execute("""
        SELECT SUM(duration), COUNT(*) 
        FROM sessions 
        WHERE strftime('%Y-%m-%d', start_time) = ?
          AND mode = 'work'
    """, (today_date,))
    
    total, count = cursor.fetchone() or (0, 0)
    return total or 0, count or 0