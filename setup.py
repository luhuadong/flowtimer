from setuptools import setup, find_packages

setup(
    name="flowtimer",
    version="0.1.0",
    author="luhuadong",
    author_email="luhuadong@163.com",
    description="A terminal Pomodoro timer with productivity stats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/luhuadong/flowtimer",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "rich>=13.0",
        "simpleaudio>=1.0.4; sys_platform == 'linux'",
        "plotext>=5.0",
        "python-dotenv>=0.19",
    ],
    entry_points={
        "console_scripts": [
            "flowtimer=flowtimer.cli:main",
        ],
    },
    license="MIT",
)