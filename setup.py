from setuptools import setup, find_packages

setup(
    name="devtools-hub",
    version="3.5.0",
    packages=find_packages(),
    install_requires=["flask", "psutil", "requests"],
    entry_points={
        "console_scripts": [
            "devtools=devtools_hub.cli:main",
            "dev=devtools_hub.cli:main"
        ]
    },
    author="jingjing737",
    description="开发者工具集 - 系统监控、进程管理",
    url="https://github.com/jingjing737/devtools-hub"
)
