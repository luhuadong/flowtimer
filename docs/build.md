# 构建 & 部署



## 构建

安装/更新构建工具：

```bash
pip install --upgrade pip setuptools wheel

# Linux 系统需要安装以下依赖
sudo apt-get install python3-gi gir1.2-gstreamer-1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good
pip install pygobject
```

进入 flowtimer 工程目录，使用开发模式安装：

```bash
pip install -e .
```

彻底卸载旧版本

```bash
pip uninstall flowtimer -y
```



## 测试

第一次运行，设置工作25分钟，休息5分钟

```bash
flowtimer start --work 25 --break 5

# 也可以只设置一个参数
flowtimer start --work 25
```

查看状态

```bash
flowtimer stats
# 应输出：今日专注时间: 1 分钟，完成番茄钟: 1 次
```

状态信息存储在 sqlite3 数据库中，可通过 SQL 语句查询：

```bash
sqlite3 ~/.flowtimer.db "SELECT * FROM sessions"
# 应看到类似：1|2024-05-20 15:30:00|1|work
```



## 部署

生成发布包

```bash
# 生成 wheel 和 sdist
python -m build
```

成功后会生成 `dist/` 目录，包含两个文件：

```bash
dist/
├── flowtimer-0.1.0-py3-none-any.whl
└── flowtimer-0.1.0.tar.gz
```

上传到 PyPI

```bash
# 上传到正式 PyPI（需输入账号密码）
twine upload dist/*
```



## 验证

打开一个新终端

```bash
# 从 PyPI 安装测试
pip uninstall flowtimer -y
pip install flowtimer

# 运行测试
flowtimer start --work 1
flowtimer stats
```

