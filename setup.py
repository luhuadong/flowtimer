from setuptools import setup, find_packages

setup(
    name="flowtimer",
    version="0.1.0",
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