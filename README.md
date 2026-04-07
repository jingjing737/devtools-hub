# DevTools Hub 🔧

> A developer toolkit for system monitoring, process management, and performance testing.
> 开发者工具集 - 系统监控、进程管理、性能测试

---

## 📦 Installation | 安装

```bash
pip install devtools-hub
```

Or from source:
```bash
git clone https://github.com/jingjing737/devtools-hub.git
cd devtools-hub
pip install -e .
```

或从源码安装：
```bash
git clone https://github.com/jingjing737/devtools-hub.git
cd devtools-hub
pip install -e .
```

---

## ⌨️ Commands | 命令

| English | 中文 | Description |
|---------|------|-------------|
| `devtools` | devtools | Show help / 显示帮助 |
| `devtools start` | devtools start | Start service / 启动服务 |
| `devtools stop` | devtools stop | Stop service / 停止服务 |
| `devtools status` | devtools status | System status / 系统状态 |
| `devtools cpu` | devtools cpu | CPU info / CPU 信息 |
| `devtools mem` | devtools mem | Memory info / 内存信息 |
| `devtools disk` | devtools disk | Disk info / 磁盘信息 |
| `devtools net` | devtools net | Network speed / 网络速度 |
| `devtools top` | devtools top | Top processes / 高占用进程 |
| `devtools ports` | devtools ports | Port scanner / 端口扫描 |
| `devtools services` | devtools services | System services / 系统服务 |
| `devtools info` | devtools info | System info / 系统信息 |
| `devtools ip` | devtools ip | IP address / IP 地址 |
| `devtools bench` | devtools bench | Performance test / 性能测试 |

---

## 📊 Examples | 示例

### Port Scanner | 端口扫描
```bash
$ devtools ports
🔍 Scanning common ports...
  ✅ 22 (SSH) - open | 开放
  ✅ 80 (HTTP) - open | 开放
  ✅ 5001 (DevTools) - open | 开放
```

### IP Address | IP 地址
```bash
$ devtools ip
Host: MacBook-Air
IP: 192.168.1.100
```

### System Info | 系统信息
```bash
$ devtools info
System: Darwin 24.6.0
Host: MacBook-Air
Python: 3.14.0

$ devtools cpu
CPU: 45%  Cores: 8

$ devtools mem
Memory: 62%  Available: 6.1GB
```

### Top Processes | 高占用进程
```bash
$ devtools top
🔥 CPU:
  python: 45.2%
  chrome: 28.1%
💾 Memory:
  chrome: 35.2%
  python: 12.3%
```

### Performance Benchmark | 性能测试
```bash
$ devtools bench
{
  "cpu_score": 245.3,
  "memory_score": 189.2,
  "disk_score": 312.8,
  "total_score": 747.3
}
```

---

## 🐳 Docker

```bash
# Build | 构建
docker build -t devtools-hub .

# Run | 运行
docker run -d -p 5001:5001 devtools-hub

# Or use docker-compose | 或使用 docker-compose
docker-compose up -d
```

---

## 🔧 Development | 开发

```bash
# Install dependencies | 安装依赖
pip install -r requirements.txt

# Run server | 运行服务
python -m devtools_hub.server

# Run CLI | 运行 CLI
python -m devtools_hub.cli

# Run tests | 运行测试
python test_api.py
```

---

## 📁 Project Structure | 项目结构

```
devtools-hub/
├── devtools_hub/
│   ├── __init__.py
│   ├── cli.py          # CLI entry | CLI 入口
│   ├── server.py       # Flask server | Flask 服务
│   └── scanner.py      # Port scanner | 端口扫描
├── setup.py
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📝 License | 许可证

MIT License

---

**GitHub**: https://github.com/jingjing737/devtools-hub  
**PyPI**: https://pypi.org/project/devtools-hub/  
**Version**: v2.6.0
