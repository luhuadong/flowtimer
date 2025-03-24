# FlowTimer 🍅⏰

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![PyPI Version](https://img.shields.io/pypi/v/flowtimer.svg)](https://pypi.org/project/flowtimer/)

[English](README.md) | [中文](README_zh.md)

FlowTimer 是一个专为开发者打造的极简命令行番茄钟，支持生产力统计。尤其适合经常在命令行（Terminal）中工作的开发者（Linux、macOS），当然 Windows 也能运行。

## 功能亮点 ✨

- ⏱️ **自定义时间**：`flowtimer work 45 --break 10`
- 🎨 **美观终端界面**：基于 `rich` 库的彩色进度条
- 🔔 **跨平台通知**：系统弹窗 + 声音提醒
- 📊 **每日统计**：`flowtimer stats` 查看专注时长
- ⏯️ **暂停/继续**：随时按 `Ctrl+P`

## 安装 📦
```bash
pip install flowtimer
```

## 快速开始 🚀

```bash
# 默认模式（25分钟专注 + 5分钟休息）
flowtimer start

# 自定义时间（45分钟专注，10分钟休息）
flowtimer start --work 45 --break 10

# 查看当日统计
flowtimer stats

# 结束时播放自定义声音
flowtimer start --sound-alert ~/ding.mp3
```

## 配置 ⚙️

创建 ~/.flowtimerrc 文件设置默认值：

```ini
[settings]
work = 25
break = 5
sound_alert = /路径/到/提示音.mp3
```

## 如何贡献 🤝

欢迎提交 Issue 或 Pull Request！

- 代码规范：遵循 PEP8
- 测试：添加 pytest 单元测试
- 文档：更新对应的中英文内容


## 开源协议 📄

本项目基于 [MIT 许可证](LICENSE) 开源。
