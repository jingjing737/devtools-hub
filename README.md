# DevTools Hub 🔧

> A developer toolkit for system monitoring, process management, and performance testing.
> 开发者工具集 - 系统监控、进程管理、性能测试

---

## English

A lightweight command-line tool for developers to monitor system resources, manage processes, scan ports, and run performance benchmarks.

**Install:**
```bash
pip install devtools-hub
```

**Commands:**
```
devtools          # Show help
devtools start    # Start service
devtools stop     # Stop service
devtools status   # System status
devtools cpu      # CPU info
devtools mem      # Memory info
devtools disk     # Disk info
devtools net      # Network speed
devtools top      # Top processes
devtools ports    # Port scanner
devtools services # System services
devtools info     # System info
devtools ip       # IP address
devtools bench    # Performance test
```

**Example:**
```bash
$ devtools ports
🔍 Scanning common ports...
  ✅ 22 (SSH) - open
  ✅ 5001 (DevTools) - open

$ devtools ip
Host: MacBook-Air
IP: 192.168.1.100
```

---

## 中文

轻量级命令行工具，用于监控系统资源、管理进程、扫描端口、运行性能测试。

**安装:**
```bash
pip install devtools-hub
```

**命令:**
```
devtools          # 显示帮助
devtools start    # 启动服务
devtools stop     # 停止服务
devtools status   # 系统状态
devtools cpu      # CPU 信息
devtools mem      # 内存信息
devtools disk     # 磁盘信息
devtools net      # 网络速度
devtools top      # 高占用进程
devtools ports    # 端口扫描
devtools services # 系统服务
devtools info     # 系统信息
devtools ip       # IP 地址
devtools bench    # 性能测试
```

**示例:**
```bash
$ devtools ports
🔍 扫描常用端口...
  ✅ 22 (SSH) - 开放
  ✅ 5001 (DevTools) - 开放

$ devtools ip
主机: MacBook-Air
IP: 192.168.1.100

$ devtools top
🔥 CPU:
  python: 45.2%
💾 内存:
  chrome: 35.2%
```

---

**GitHub**: https://github.com/jingjing737/devtools-hub  
**PyPI**: https://pypi.org/project/devtools-hub/  
**Version**: v2.6.0
