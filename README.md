# FlowTimer 🍅⏰

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

[中文](README_zh.md) | [English](README.md)

A minimalist command-line Pomodoro timer with productivity stats, built for developers who love the terminal.

## Features ✨

- ⏱️ **Customizable intervals**: `flowtimer work 45 --break 10`
- 🎨 **Beautiful terminal UI**: Progress bars with `rich` library
- 🔔 **Cross-platform notifications**: System alerts + sound
- 📊 **Daily stats**: Track your focus time via `flowtimer stats`
- ⏯️ **Pause/Resume**: Press `Ctrl+P` anytime

## Installation 📦

```bash
pip install flowtimer
```

## Quick Start 🚀

```bash
# Start a default session (25min work + 5min break)
flowtimer start

# Customize time (45min work, 10min break)
flowtimer start --work 45 --break 10

# Show today's stats
flowtimer stats

# Play a custom sound on finish
flowtimer start --sound-alert ~/ding.mp3
```

## Configuration ⚙️

Create ~/.flowtimerrc to set defaults:

```ini
[settings]
work = 25
break = 5
sound_alert = /path/to/sound.mp3
```

## Contributing 🤝

Issues and PRs are welcome!

- Code Style: Follow PEP8
- Testing: Add pytest unit tests
- Docs: Update English or Chinese documentation

## License 📄

Licensed under the [MIT License](LICENSE).