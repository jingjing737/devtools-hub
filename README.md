# DevTools Hub 🔧

> A developer toolkit for system monitoring, process management, and performance testing.
> 开发者工具集 - 系统监控、进程管理、性能测试

---

## 📦 Installation | 安装

### Homebrew (macOS)
```bash
brew tap jingjing737/tap
brew install devtools-hub
```

### pip
```bash
pip install devtools-hub
```

### 从源码安装
```bash
git clone https://github.com/jingjing737/devtools-hub.git
cd devtools-hub
pip install -e .
```

---

## ⌨️ Commands | 命令 (176 commands)

### 🖥️ System Monitoring | 系统监控
| English | 中文 | Description |
|---------|------|-------------|
| `devtools cpu` | devtools cpu | CPU info / CPU 信息 |
| `devtools cpu-usage` | devtools cpu-usage | Detailed CPU usage / 详细 CPU 使用率 |
| `devtools mem` | devtools mem | Memory info / 内存信息 |
| `devtools disk` | devtools disk | Disk info / 磁盘信息 |
| `devtools df` | devtools df | Disk filesystem / 磁盘文件系统 |
| `devtools battery` | devtools battery | Battery status / 电池状态 |
| `devtools temp` | devtools temp | Temperature / 温度 |
| `devtools uptime` | devtools uptime | System uptime / 运行时间 |
| `devtools load` | devtools load | System load / 系统负载 |
| `devtools sysinfo` | devtools sysinfo | System info / 系统信息 |
| `devtools neofetch` | devtools neofetch | System info display / 系统信息展示 |
| `devtools pmset` | devtools pmset | Power management / 电源管理 |

### 🌐 Network | 网络
| English | 中文 | Description |
|---------|------|-------------|
| `devtools ip` | devtools ip | Local IP / 本地 IP |
| `devtools publicip` | devtools publicip | Public IP / 公网 IP |
| `devtools ipinfo` | devtools ipinfo | IP info lookup / IP 信息查询 |
| `devtools ping` | devtools ping | Ping host /  Ping 主机 |
| `devtools dns` | devtools dns | DNS lookup / DNS 查询 |
| `devtools nslookup` | devtools nslookup | NS lookup / 域名解析 |
| `devtools host` | devtools host | Host lookup / 主机查询 |
| `devtools ifconfig` | devtools ifconfig | Network interfaces / 网络接口 |
| `devtools speed` | devtools speed | Network speed / 网速 |
| `devtools wifi` | devtools wifi | WiFi info / WiFi 信息 |
| `devtools tracert` | devtools tracert | Traceroute / 路由追踪 |
| `devtools netstat` | devtools netstat | Network stats / 网络统计 |
| `devtools ssh` | devtools ssh | SSH connect / SSH 连接 |
| `devtools scp` | devtools scp | Secure copy / 安全复制 |
| `devtools rsync` | devtools rsync | Rsync sync / 文件同步 |
| `devtools wget` | devtools wget | Download file / 下载文件 |
| `devtools curl-post` | devtools curl-post | POST request / POST 请求 |
| `devtools curl-headers` | devtools curl-headers | HTTP headers / HTTP 头 |
| `devtools shorten` | devtools shorten | URL shorten / 缩短 URL |
| `devtools qr` | devtools qr | Generate QR code / 生成二维码 |

### 📊 Process Management | 进程管理
| English | 中文 | Description |
|---------|------|-------------|
| `devtools top` | devtools top | Top processes / 高占用进程 |
| `devtools ps` | devtools ps | Process list / 进程列表 |
| `devtools kill` | devtools kill | Kill process / 终止进程 |
| `devtools zombie` | devtools zombie | Zombie processes / 僵尸进程 |
| `devtools process` | devtools process | Process detail / 进程详情 |
| `devtools children` | devtools children | Child processes / 子进程 |
| `devtools watch` | devtools watch | Watch process / 监控进程 |
| `devtools lsof` | devtools lsof | Open files / 打开文件 |
| `devtools pgrep` | devtools pgrep | Search process / 搜索进程 |
| `devtools pkill` | devtools pkill | Kill by name / 按名终止 |
| `devtools running` | devtools running | Running apps / 运行应用 |

### 🔧 System Tools | 系统工具
| English | 中文 | Description |
|---------|------|-------------|
| `devtools launchctl` | devtools launchctl | Launchctl manager / 启动服务管理 |
| `devtools crontab` | devtools crontab | Crontab editor / 定时任务 |
| `devtools lock` | devtools lock | Lock screen / 锁屏 |
| `devtools restart` | devtools restart | Restart system / 重启系统 |
| `devtools shutdown` | devtools shutdown | Shutdown system / 关机 |
| `devtools clearlogs` | devtools clearlogs | Clear logs / 清理日志 |
| `devtools alias` | devtools alias | Show aliases / 显示别名 |

### 🐙 Git | Git 版本控制
| English | 中文 | Description |
|---------|------|-------------|
| `devtools git` | devtools git | Git status / Git 状态 |
| `devtools gstatus` | devtools gstatus | Git detailed status / 详细状态 |
| `devtools glog` | devtools glog | Git log / Git 日志 |
| `devtools glog2` | devtools glog2 | Git graph log / Git 图形日志 |
| `devtools gbranch` | devtools gbranch | Git branches / Git 分支 |
| `devtools gpull` | devtools gpull | Git pull / Git 拉取 |
| `devtools gpush` | devtools gpush | Git push / Git 推送 |
| `devtools gstash` | devtools gstash | Git stash list / Git 暂存列表 |
| `devtools gclean` | devtools gclean | Clean branches / 清理分支 |
| `devtools gundo` | devtools gundo | Undo last commit / 撤销提交 |
| `devtools gfork` | devtools gfork | Fork rebase / Fork rebase |

### 🐳 Docker | Docker 容器
| English | 中文 | Description |
|---------|------|-------------|
| `devtools dps` | devtools dps | Docker ps / 容器列表 |
| `devtools dpsa` | devtools dpsa | Docker ps all / 所有容器 |
| `devtools dimages` | devtools dimages | Docker images / 镜像列表 |
| `devtools dstop` | devtools dstop | Stop all containers / 停止所有容器 |
| `devtools drm` | devtools drm | Remove containers / 清理容器 |
| `devtools dlogs` | devtools dlogs | Container logs / 容器日志 |
| `devtools dexec` | devtools dexec | Exec command / 执行命令 |

### 📁 File Tools | 文件工具
| English | 中文 | Description |
|---------|------|-------------|
| `devtools du` | devtools du | Disk usage / 磁盘使用 |
| `devtools find` | devtools find | Find files / 查找文件 |
| `devtools find2` | devtools find2 | Find by size / 按大小查找 |
| `devtools size` | devtools size | File size / 文件大小 |
| `devtools lines` | devtools lines | Count lines / 统计行数 |
| `devtools tree` | devtools tree | Directory tree / 目录树 |
| `devtools preview` | devtools preview | Preview file / 预览文件 |
| `devtools compare` | devtools compare | Compare files / 对比文件 |
| `devtools diff` | devtools diff | File diff / 文件差异 |
| `devtools mime` | devtools mime | MIME type / MIME 类型 |
| `devtools extract` | devtools extract | Extract archive / 解压文件 |
| `devtools backup` | devtools backup | Backup file / 备份文件 |
| `devtools clipboard` | devtools clipboard | Clipboard content / 剪贴板 |

### 🔍 Search & Text | 搜索文本
| English | 中文 | Description |
|---------|------|-------------|
| `devtools grep` | devtools grep | Search text / 搜索文本 |
| `devtools ports` | devtools ports | Port scan / 端口扫描 |
| `devtools services` | devtools services | System services / 系统服务 |
| `devtools jq` | devtools jq | JSON processor / JSON 处理 |
| `devtools color` | devtools color | Color converter / 颜色转换 |

### 🛠️ Development | 开发工具
| English | 中文 | Description |
|---------|------|-------------|
| `devtools npm-outdated` | devtools npm-outdated | npm outdated / 检查过期包 |
| `devtools pip-list` | devtools pip-list | pip outdated / pip 过期包 |
| `devtools yarn` | devtools yarn | Yarn runner / Yarn 运行 |
| `devtools pnpm` | devtools pnpm | pnpm runner / pnpm 运行 |
| `devtools bun` | devtools bun | Bun runner / Bun 运行 |
| `devtools cargo` | devtools cargo | Cargo runner / Cargo 运行 |
| `devtools gcc` | devtools gcc | GCC compiler / GCC 编译 |
| `devtools make` | devtools make | Make build / Make 构建 |
| `devtools cmake` | devtools cmake | CMake build / CMake 构建 |
| `devtools whatis` | devtools whatis | Command info / 命令说明 |

### 🔐 Security & Hash | 安全哈希
| English | 中文 | Description |
|---------|------|-------------|
| `devtools hash` | devtools hash | Hash calculator / 哈希计算 |
| `devtools md5` | devtools md5 | MD5 hash / MD5 哈希 |
| `devtools sha1` | devtools sha1 | SHA1 hash / SHA1 哈希 |
| `devtools sha256` | devtools sha256 | SHA256 hash / SHA256 哈希 |
| `devtools pass` | devtools pass | Password generator / 密码生成 |

### 🌐 Web & API | Web API
| English | 中文 | Description |
|---------|------|-------------|
| `devtools curl` | devtools curl | HTTP request / HTTP 请求 |
| `devtools headers` | devtools headers | HTTP headers / HTTP 头 |
| `devtools json` | devtools json | JSON formatter / JSON 格式化 |
| `devtools base64` | devtools base64 | Base64 encode/decode / Base64 编解码 |
| `devtools url` | devtools url | URL encode/decode / URL 编解码 |

### ☁️ Cloud & Services | 云服务
| English | 中文 | Description |
|---------|------|-------------|
| `devtools github` | devtools github | GitHub info / GitHub 信息 |
| `devtools pypi` | devtools pypi | PyPI info / PyPI 信息 |
| `devtools weather` | devtools weather | Weather info / 天气信息 |

### 🎨 Fun & Utils | 趣味工具
| English | 中文 | Description |
|---------|------|-------------|
| `devtools say` | devtools say | Text to speech / 语音朗读 |
| `devtools fortune` | devtools fortune | Fortune cookie / 随机语录 |
| `devtools sl` | devtools sl | Steam locomotive / 蒸汽火车 |
| `devtools hack` | devtools hack | ASCII hack / ASCII 黑客 |
| `devtools meow` | devtools meow | Cat ASCII / 猫咪 ASCII |
| `devtools banana` | devtools banana | Banana / 香蕉 |
| `devtools rocket` | devtools rocket | Rocket ASCII / 火箭 ASCII |
| `devtools countdown` | devtools countdown | Countdown timer / 倒计时 |
| `devtools pomodoro` | devtools pomodoro | Pomodoro timer / 番茄钟 |
| `devtools spin` | devtools spin | Loading spinner / 加载动画 |

### 🍎 macOS | macOS 特有
| English | 中文 | Description |
|---------|------|-------------|
| `devtools caffeinate` | devtools caffeinate | Prevent sleep / 防止休眠 |
| `devtools qrdecode` | devtools qrdecode | Generate QR / 生成二维码 |

---

## 🚀 Quick Start | 快速开始

```bash
# 安装
pip install devtools-hub

# 查看帮助
devtools

# 系统状态
devtools status

# 端口扫描
devtools ports

# 性能测试
devtools bench

# 启动 Web 服务
devtools start
```

---

## 📊 Examples | 示例

### System Status | 系统状态
```bash
$ devtools status
🖥️  System: Darwin 24.6.0
💾  Memory: 62%  Available: 6.1GB
🔥  CPU: 45%
🔋  Battery: 78%
⏰  Uptime: 3 days
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

## 📝 Releases | 版本发布

### v3.4.0 (2026-04-08)
- 新增 62 个命令，总计 176 个命令
- Git 增强: glog2, gstash, gclean, gundo, gfork
- Docker 增强: dps, dpsa, dimages, dstop, drm, dlogs, dexec
- 系统工具: launchctl, crontab, lock, restart, shutdown
- 网络工具: ssh, scp, rsync, wget, curl-post, curl-headers
- 开发工具: npm-outdated, pip-list, yarn, pnpm, bun, cargo
- 趣味工具: fortune, sl, hack, meow, banana, countdown, pomodoro
- 修复多个 bug

### v3.0.0 (2026-04-07)
- 重大更新，命令从 64 个扩展到 114 个
- 发布到 PyPI

### v2.6.0 (2026-04-07)
- 中英文双语 README
- Homebrew 支持

---

## 📝 License | 许可证

MIT License

---

**GitHub**: https://github.com/jingjing737/devtools-hub  
**Homebrew**: https://github.com/jingjing737/homebrew-tap  
**PyPI**: https://pypi.org/project/devtools-hub/  
**Version**: v3.4.0
