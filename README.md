# DevTools Hub 🔧

> 开发者工具集 - 系统监控、进程管理

## 📦 安装

```bash
pip install devtools-hub
```

## ⌨️ 命令

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

## 📊 示例

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
