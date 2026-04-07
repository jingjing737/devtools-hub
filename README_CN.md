# DevTools Hub 🚀

> All-in-one developer toolkit. 一个全栈开发者工具箱。

[English](./README.md) | [中文](./README_CN.md)

[![Stars](https://img.shields.io/github/stars/jingjing737/devtools-hub?style=flat)](https://github.com/jingjing737/devtools-hub/stargazers)
[![License](https://img.shields.io/github/license/jingjing737/devtools-hub)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Node](https://img.shields.io/badge/Node-18+-green)

## ✨ 功能特性

- 🖥️ **控制面板** - Web 端控制面板
- 🔧 **CLI 工具** - 开发者必备命令
- 📊 **数据分析** - 项目监控与指标
- 🤖 **AI 集成** - 内置 AI 辅助
- 🔄 **自动化** - 工作流自动化
- 📁 **文件管理** - 云端文件管理

## 📦 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/jingjing737/devtools-hub.git
cd devtools-hub

# 安装依赖
pip install -r requirements.txt
# 或
npm install
```

### 启动控制面板

```bash
# Python
python dashboard/app.py

# Node
node dashboard/app.js
```

访问地址：`http://localhost:5000`

## 📁 项目结构

```
devtools-hub/
├── dashboard/          # Web 控制面板
│   ├── static/         # CSS, JS, 图片资源
│   ├── templates/     # HTML 模板
│   └── app.py         # Flask 应用
├── cli/                # 命令行工具
├── automation/        # 自动化脚本
├── analytics/         # 数据分析与监控
├── ai/                # AI 集成
└── docs/              # 文档
```

## 🛠️ 工具列表

### 控制面板功能

| 功能 | 说明 |
|------|------|
| 系统监控 | CPU、内存、磁盘使用情况 |
| 进程管理 | 查看与管理进程 |
| 文件浏览器 | 浏览项目文件 |
| Git 面板 | Git 操作 UI |
| 日志查看器 | 实时日志流 |
| API 测试器 | REST API 测试 |

### CLI 命令

```bash
# 系统信息
devtools sysinfo

# 进程管理
devtools ps
devtools kill <pid>

# Git 助手
devtools git status
devtools git log

# 文件操作
devtools ls
devtools find <pattern>
```

## 🔌 集成

- **OpenClaw** - 自动化框架
- **GitHub** - 仓库管理
- **Notion** - 笔记与文档
- **Slack** - 通知
- **Webhooks** - 自定义集成

## 📊 数据分析

追踪你的开发指标：

- 代码提交趋势
- 语言分布
- 项目复杂度
- 团队活动

## 🤖 AI 功能

- 代码审查助手
- Bug 检测
- 优化建议
- 自然语言查询

## 📝 文档

详细文档见 [docs/](docs/)：

- [安装指南](docs/install.md)
- [控制面板指南](docs/dashboard.md)
- [CLI 参考](docs/cli.md)
- [API 参考](docs/api.md)

## 🤝 贡献

欢迎贡献！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📜 许可证

MIT 许可证 - 见 [LICENSE](LICENSE)

---

<p align="center">
  ⭐ 在 GitHub 上 Star 我们
</p>