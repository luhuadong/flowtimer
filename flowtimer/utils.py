import os
import sqlite3
from datetime import datetime
import platform
from playsound import playsound

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
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO sessions (duration, mode) VALUES (?, ?)", (duration, mode))
    conn.commit()
    conn.close()

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
        playsound(sound_path)
    except Exception as e:
        print(f"播放声音失败: {e}")

def get_daily_stats():
    conn = sqlite3.connect(DB_PATH)
    today = datetime.now().strftime("%Y-%m-%d")
    cursor = conn.execute("""
        SELECT SUM(duration), COUNT(*) 
        FROM sessions 
        WHERE DATE(start_time) = ? AND mode = 'work'
    """, (today,))
    total, count = cursor.fetchone()
    return total or 0, count or 0