import click
from .timer import PomodoroTimer
from .utils import init_db, get_daily_stats
from .config import load_config

@click.group()
def main():
    """FlowTimer - 终端番茄钟工具"""
    init_db()  # 初始化数据库

@main.command()
@click.option("--work", default=25, help="专注时长（分钟）")
@click.option("--break", "break_", default=5, help="休息时长（分钟）")
@click.option("--sound", default=None, help="自定义提示音文件路径")
def start(work, break_, sound):
    """启动番茄钟"""
    config = load_config()
    timer = PomodoroTimer(
        work_time=work,
        break_time=break_,
        sound_alert=sound or config.get("sound_alert")
    )
    timer.run()

@main.command()
def stats():
    """显示统计数据"""
    daily_total, completed_count = get_daily_stats()  # 重命名变量

    click.echo(f"今日专注时间: {daily_total} 分钟")
    click.echo(f"完成番茄钟: {completed_count} 次")

if __name__ == "__main__":
    main()