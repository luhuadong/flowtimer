import time
import threading
from rich.progress import Progress
from .utils import send_notification, play_sound, save_record

class PomodoroTimer:
    def __init__(self, work_time=25, break_time=5, sound_alert=None):
        self.work_time = work_time * 60
        self.break_time = break_time * 60
        self.sound_alert = sound_alert
        self.is_paused = False
        self.current_mode = "work"

    def run(self):
        with Progress() as progress:
            task = progress.add_task(f"[cyan]{self.current_mode.capitalize()}...", total=self.work_time)
            while True:
                if self.is_paused:
                    time.sleep(1)
                    continue
                
                time.sleep(1)
                progress.update(task, advance=1)
                
                if progress.tasks[task].completed >= self.work_time:
                    self._handle_finish(progress)
                    break

    def _handle_finish(self, progress):
        # 保存记录到数据库
        print(f"[DEBUG] 保存记录: duration={self.work_time//60}, mode={self.current_mode}")
        save_record(self.work_time // 60, self.current_mode)
        
        # 发送通知和声音
        message = "专注结束！该休息了！" if self.current_mode == "work" else "休息结束！"
        send_notification(message)
        if self.sound_alert:
            play_sound(self.sound_alert)
        
        # 切换模式
        self.current_mode = "break" if self.current_mode == "work" else "work"
        progress.reset(task_id=0, total=self.break_time)