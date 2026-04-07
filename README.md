# DevTools Hub 🔧

> 开发者工具集 - 系统监控、进程管理、性能测试

## 📦 安装

```bash
git clone https://github.com/jingjing737/devtools-hub.git && cd devtools-hub && ./devtools start
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
devtools kill <pid>  # 杀死进程
devtools bench    # 性能测试
```

## 📊 示例

```bash
$ devtools top
🔥 CPU:
  python: 45.2%
  chrome: 28.1%

$ devtools net
↑12.5 Mbps  ↓85.3 Mbps
```

---

**GitHub**: https://github.com/jingjing737/devtools-hub
