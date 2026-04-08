#!/usr/bin/env python3
"""DevTools Hub CLI v3.0.0 - 开发者工具集"""
import sys
import json
import time
import platform
import os
import hashlib
import base64
import socket
import re
import urllib.request
import urllib.error
import urllib.parse
import datetime
import glob
import shutil
import subprocess
import secrets
import string
import uuid
import struct
import zlib

PORT = 5001
URL = f"http://localhost:{PORT}"

def check():
    try:
        r = requests.get(f"{URL}/api/health", timeout=1)
        return r.ok
    except:
        return False

def main():
    if len(sys.argv) < 2:
        print("""
🔧 DevTools Hub v3.2.0 - 开发者工具集

用法: devtools <命令>  或  dev <命令>

📊 系统监控:
  status      系统状态
  cpu         CPU 信息
  cpu-usage   CPU 使用率趋势
  mem         内存信息
  disk        磁盘信息
  df          磁盘空间
  battery     电池状态
  temp        温度监控
  uptime      运行时间
  load        系统负载
  sysinfo     详细系统信息

🌐 网络工具:
  ip          本机 IP
  publicip    公网 IP
  ping        Ping 测试
  dns         DNS 查询
  speed       网速测试
  wifi        WiFi 信息
  tracert     路由追踪
  netstat     网络连接
  curl        HTTP 请求
  headers     HTTP 头
  iftop       网络接口流量
  nslookup    DNS 详细查询
  host        主机查询
  ifconfig    网络接口

📂 文件工具:
  du          磁盘使用
  find        查找大文件
  find2       查找文件
  size        文件大小
  wc          行数统计
  hash        计算哈希
  md5         MD5 校验
  sha1        SHA1 校验
  sha256      SHA256 校验
  json        JSON 工具
  base64      Base64 编解码
  url         URL 编解码
  env         环境变量
  tree        目录树
  preview     预览文件
  compare     文件比较
  mime        文件类型
  diff        文件差异
  grep        文本搜索
  lines       显示指定行
  cat         显示文件内容

🔧 进程管理:
  top         高占用进程
  ps          进程列表
  kill        结束进程
  zombie      僵尸进程
  children    子进程查看
  process     进程详情
  watch       监控命令输出

💻 开发工具:
  ports       端口扫描
  services    系统服务
  git         Git 状态
  gstatus     Git 状态
  glog        Git 日志
  gbranch     Git 分支
  gpull       Git 拉取
  gpush       Git 推送
  node        Node.js 信息
  python      Python 版本
  which       查找命令
  npm         npm 包管理
  pip3        pip 包管理
  brew        Homebrew 信息
  docker      Docker 容器
  dlog        Docker 日志
  gh          GitHub CLI
  code        VS Code

🛠️ 系统工具:
  info        系统信息
  bench       性能测试
  clean       清理缓存
  update      检查更新
  selfupdate  一键自更新
  start       启动服务
  stop        停止服务
  date        日期时间
  cal         日历
  who         当前用户
  history     命令历史
  aliases     所有别名
  pwd         当前目录
  cd          切换目录
  ls          列出文件
  open        打开文件/URL
  run         运行脚本

📋 剪贴板 & 截图:
  clip        获取剪贴板
  clips       设置剪贴板
  screenshot  截图
  record      屏幕录制

🔔 通知 & 提醒:
  notify      发送通知
  remind      定时提醒
  timer       计时器
  stopwatch   秒表

🔐 工具箱:
  uuid        生成 UUID
  password    生成密码
  rand        随机数
  hex         十六进制转换
  ascii       ASCII 码转换
  epoch       时间戳转换
  now         当前时间戳
  encode      编码检测
  compress    压缩数据

🖥️ macOS 设置:
  volume      音量控制
  mute        静音切换
  brightness  屏幕亮度
  theme       主题模式
  nightshift  夜览模式
  dnd         勿扰模式

📦 安装 & 服务:
  install     安装应用
  uninstall   卸载应用
  running     运行中的应用
  processes   后台进程

🧮 实用工具:
  calc        快速计算器
  server      HTTP 服务器
  path        PATH 环境变量
  port        端口占用查询
  copy        复制到剪贴板
  paste       读取剪贴板
  filesize    文件大小转换
  qr          生成二维码
  jwt         JWT 解码
  urldecode   URL 解码
  urlencode   URL 编码
  crontab     查看/管理定时任务
  clipboard   剪贴板操作
  extract     压缩包解压
  download    下载文件
  whois       域名查询
  myip        查看本机所有IP
""")
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    # ========== 系统监控 ==========
    if cmd == "status":
        if check():
            r = requests.get(f"{URL}/api/health")
            print(json.dumps(r.json(), indent=2))
        else:
            print("❌ 服务未运行，请先 devtools start")

    elif cmd == "cpu":
        import psutil
        print(f"CPU: {psutil.cpu_percent()}%  核心: {psutil.cpu_count()}  物理核心: {psutil.cpu_count(logical=False)}")

    elif cmd == "cpu-usage":
        import psutil
        print("📊 CPU 使用率（5秒采样）...")
        for i in range(5):
            print(f"  {psutil.cpu_percent(interval=1)}%", end=" ", flush=True)
        print()

    elif cmd == "mem":
        import psutil
        m = psutil.virtual_memory()
        print(f"内存: {m.percent}%  已用: {m.used/1024**3:.1f}GB  可用: {m.available/1024**3:.1f}GB  总计: {m.total/1024**3:.1f}GB")
        s = psutil.swap_memory()
        print(f"Swap: {s.percent}%  已用: {s.used/1024**3:.1f}GB")

    elif cmd == "disk":
        import psutil
        for p in ['/', '/System/Volumes/Data', '/Users']:
            try:
                d = psutil.disk_usage(p)
                print(f"{p}: {d.percent}%  已用: {d.used/1024**3:.1f}GB  可用: {d.free/1024**3:.1f}GB")
            except:
                pass

    elif cmd == "df":
        os.system('df -h')

    elif cmd == "battery":
        import psutil
        try:
            b = psutil.sensors_battery()
            if b:
                print(f"电池: {b.percent}% {'🔌 充电中' if b.power_plugged else '🔋 使用电池'}")
                if b.secsleft and b.secsleft > 0:
                    h = b.secsleft // 3600
                    m = (b.secsleft % 3600) // 60
                    print(f"剩余时间: {h}h {m}m")
            else:
                print("❌ 无电池（台式机）")
        except:
            print("❌ 电池信息不可用")

    elif cmd == "temp":
        import psutil
        temps = getattr(psutil, 'sensors_temperatures', lambda: {})()
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    label = entry.label or name
                    current = entry.current
                    high = entry.high or "N/A"
                    print(f"🌡️ {label}: {current:.1f}°C  最高: {high}°C")
        else:
            print("❌ 温度信息不可用")

    elif cmd == "uptime":
        import psutil
        boot = psutil.boot_time()
        now = datetime.datetime.now()
        boot_time = datetime.datetime.fromtimestamp(boot)
        delta = now - boot_time
        print(f"系统运行: {delta.days}天 {delta.seconds//3600}小时 {(delta.seconds%3600)//60}分钟")
        print(f"启动时间: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

    elif cmd == "load":
        load = os.getloadavg() if hasattr(os, 'getloadavg') else (0, 0, 0)
        print(f"负载: {load[0]:.2f} {load[1]:.2f} {load[2]:.2f} (1/5/15分钟)")

    elif cmd == "sysinfo":
        import psutil
        print(f"""
🖥️  详细系统信息:

系统:
  操作系统: {platform.system()} {platform.release()}
  版本: {platform.mac_ver()[0]}
  架构: {platform.machine()}
  主机名: {platform.node()}

处理器:
  类型: {platform.processor() or 'Apple Silicon'}
  物理核心: {psutil.cpu_count(logical=False)}
  逻辑核心: {psutil.cpu_count(logical=True)}

内存:
  总计: {psutil.virtual_memory().total/1024**3:.1f} GB
  可用: {psutil.virtual_memory().available/1024**3:.1f} GB
  使用率: {psutil.virtual_memory().percent}%

磁盘:
  总计: {psutil.disk_usage('/').total/1024**3:.1f} GB
  已用: {psutil.disk_usage('/').used/1024**3:.1f} GB
  可用: {psutil.disk_usage('/').free/1024**3:.1f} GB

Python:
  版本: {platform.python_version()}
  路径: {sys.executable}
""")

    # ========== 网络工具 ==========
    elif cmd == "ip":
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print(f"主机: {hostname}")
            print(f"IP: {ip}")
        except:
            print(f"IP: {socket.gethostbyname(socket.gethostname())}")

    elif cmd == "publicip":
        try:
            ip = urllib.request.urlopen('https://api.ipify.org', timeout=5).read().decode()
            print(f"🌐 公网IP: {ip}")
            try:
                data = urllib.request.urlopen(f'https://ipapi.co/{ip}/json/', timeout=5).read().decode()
                loc = json.loads(data)
                print(f"📍 位置: {loc.get('city', '')}, {loc.get('country_name', '')}")
                print(f"🏢 运营商: {loc.get('org', '')}")
            except:
                pass
        except Exception as e:
            print(f"❌ api.ipify.org 不可用，尝试备用方案...")
            try:
                import urllib.parse
                data = urllib.request.urlopen('https://icanhazip.com', timeout=5).read().decode().strip()
                print(f"🌐 公网IP: {data}")
            except:
                print(f"❌ 获取失败: {e}")

    elif cmd == "ping":
        if not args:
            args = ['8.8.8.8']
        host = args[0]
        print(f"📡 Ping {host}...")
        os.system(f'ping -c 4 {host}')

    elif cmd == "dns":
        if not args:
            print("用法: devtools dns <域名>")
            return
        domain = args[0]
        print(f"🔍 DNS 查询: {domain}")
        try:
            ip = socket.gethostbyname(domain)
            print(f"✅ 解析: {ip}")
        except Exception as e:
            print(f"❌ 解析失败: {e}")

    elif cmd == "nslookup":
        if not args:
            args = ['8.8.8.8']
        os.system(f'nslookup {args[0]}')

    elif cmd == "host":
        if not args:
            print("用法: devtools host <域名>")
            return
        os.system(f'host {args[0]}')

    elif cmd == "ifconfig":
        os.system('ifconfig | head -30')

    elif cmd == "speed":
        print("📊 测速中（下载测试）...")
        try:
            start = time.time()
            urllib.request.urlopen('https://speed.cloudflare.com/__down?bytes=10000000', timeout=30)
            elapsed = time.time() - start
            speed = 10 / elapsed
            print(f"⚡ 网速: {speed:.1f} MB/s ({(speed*8):.1f} Mbps)")
        except Exception as e:
            print(f"❌ 测速失败: {e}")

    elif cmd == "wifi":
        os.system('networksetup -listallhardwareports')

    elif cmd == "tracert":
        if not args:
            args = ['8.8.8.8']
        host = args[0]
        print(f"🛤️ 路由追踪: {host}")
        os.system(f'traceroute -m 15 {host}')

    elif cmd == "netstat":
        import psutil
        print("🔌 网络连接:")
        try:
            connections = psutil.net_connections(kind='inet')
            listening = [c for c in connections if c.status == 'LISTEN']
            established = [c for c in connections if c.status == 'ESTABLISHED']
            print(f"  监听中: {len(listening)}")
            print(f"  已连接: {len(established)}")
        except PermissionError:
            print("  ⚠️ 需要 sudo 权限查看详细连接")
            print("  💡 使用 'lsof -i' 查看网络连接")

    elif cmd == "curl":
        if not args:
            print("用法: devtools curl <URL>")
            return
        url = args[0]
        print(f"📡 GET {url}")
        try:
            req = urllib.request.urlopen(url, timeout=10)
            content = req.read(2000).decode('utf-8', errors='ignore')
            print(f"\n状态: {req.status}")
            print(f"内容:\n{content[:500]}")
        except Exception as e:
            print(f"❌ 请求失败: {e}")

    elif cmd == "headers":
        if not args:
            print("用法: devtools headers <URL>")
            return
        url = args[0]
        try:
            req = urllib.request.urlopen(url, timeout=10)
            print(f"📋 HTTP Headers ({url}):")
            for k, v in req.headers.items():
                print(f"  {k}: {v}")
        except Exception as e:
            print(f"❌ 请求失败: {e}")

    elif cmd == "iftop":
        import psutil
        net1 = psutil.net_io_counters()
        time.sleep(1)
        net2 = psutil.net_io_counters()
        sent = (net2.bytes_sent - net1.bytes_sent) / 1024
        recv = (net2.bytes_recv - net1.bytes_recv) / 1024
        print(f"📶 网络流量（1秒）:")
        print(f"  ↑ 发送: {sent:.1f} KB/s")
        print(f"  ↓ 接收: {recv:.1f} KB/s")

    # ========== 进程管理 ==========
    elif cmd == "top":
        import psutil
        procs = []
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username']):
            try:
                procs.append(p.info)
            except:
                pass
        by_cpu = sorted(procs, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:8]
        by_mem = sorted(procs, key=lambda x: x['memory_percent'] or 0, reverse=True)[:5]
        print("🔥 CPU 高占用:")
        for p in by_cpu:
            print(f"  PID {p['pid']:>6} | {p['name'][:25]:<25} | {p['cpu_percent']:>5}% | {p.get('username', '')[:15]}")
        print("\n💾 内存高占用:")
        for p in by_mem:
            print(f"  PID {p['pid']:>6} | {p['name'][:25]:<25} | {p['memory_percent']:>5}%")

    elif cmd == "ps":
        import psutil
        procs = []
        for p in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
            try:
                procs.append(p.info)
            except:
                pass
        print(f"📋 总进程数: {len(procs)}")
        running = sum(1 for p in procs if p.get('status') == 'running')
        sleeping = sum(1 for p in procs if p.get('status') == 'sleeping')
        print(f"   运行中: {running}  睡眠中: {sleeping}")

    elif cmd == "kill":
        if not args:
            print("用法: devtools kill <进程名或PID>")
            return
        target = args[0]
        try:
            pid = int(target)
            p = psutil.Process(pid)
            name = p.name()
            p.kill()
            print(f"✅ 已结束进程: {name} (PID: {pid})")
        except ValueError:
            killed = 0
            for p in psutil.process_iter(['pid', 'name']):
                try:
                    if target.lower() in p.info['name'].lower():
                        p.kill()
                        killed += 1
                except:
                    pass
            print(f"✅ 已结束 {killed} 个进程: {target}")
        except Exception as e:
            print(f"❌ 结束进程失败: {e}")

    elif cmd == "zombie":
        import psutil
        zombies = []
        for p in psutil.process_iter(['pid', 'name', 'status']):
            try:
                if p.info['status'] == 'zombie':
                    zombies.append(p.info)
            except:
                pass
        if zombies:
            print(f"🧟 僵尸进程 ({len(zombies)}):")
            for z in zombies:
                print(f"  PID {z['pid']}: {z['name']}")
        else:
            print("✅ 无僵尸进程")

    elif cmd == "process":
        if not args:
            print("用法: devtools process <PID或名称>")
            return
        target = args[0]
        p = None
        try:
            pid = int(target)
            p = psutil.Process(pid)
        except:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if target.lower() in proc.info['name'].lower():
                        p = psutil.Process(proc.info['pid'])
                        break
                except:
                    pass
        if p:
            print(f"📋 进程信息: {p.name()}")
            print(f"  PID: {p.pid}")
            print(f"  状态: {p.status()}")
            print(f"  CPU: {p.cpu_percent()}%")
            print(f"  内存: {p.memory_info().rss/1024**2:.1f} MB")
            print(f"  线程: {p.num_threads()}")
            print(f"  启动: {datetime.datetime.fromtimestamp(p.create_time()).strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"❌ 未找到进程: {target}")

    elif cmd == "children":
        if not args:
            print("用法: devtools children <PID或名称>")
            return
        target = args[0]
        p = None
        try:
            pid = int(target)
            p = psutil.Process(pid)
        except:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if target.lower() in proc.info['name'].lower():
                        p = psutil.Process(proc.info['pid'])
                        break
                except:
                    pass
        if p:
            children = p.children(recursive=True)
            if children:
                print(f"👶 子进程 ({len(children)}):")
                for c in children[:20]:
                    try:
                        print(f"  PID {c.pid}: {c.name()}")
                    except:
                        pass
            else:
                print("❌ 无子进程")
        else:
            print(f"❌ 未找到进程: {target}")

    elif cmd == "watch":
        if not args:
            print("用法: devtools watch <命令> [间隔秒数]")
            return
        interval = int(args[-1]) if args[-1].isdigit() else 2
        watch_cmd = args[:-1] if args[-1].isdigit() else args
        print(f"👀 监控命令: {' '.join(watch_cmd)} (每 {interval} 秒)")
        try:
            while True:
                os.system('clear')
                print(f"🕐 {datetime.datetime.now().strftime('%H:%M:%S')}")
                subprocess.run(' '.join(watch_cmd), shell=True)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n✅ 已停止监控")

    # ========== 文件工具 ==========
    elif cmd == "du":
        if not args:
            path = os.path.expanduser('~')
        else:
            path = os.path.expanduser(args[0])
        print(f"📁 磁盘使用: {path}")
        os.system(f'du -sh "{path}"')

    elif cmd == "find":
        print("🔍 查找大文件...")
        home = os.path.expanduser('~')
        files = []
        for root, dirs, filenames in os.walk(home):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for f in filenames:
                fp = os.path.join(root, f)
                try:
                    size = os.path.getsize(fp)
                    if size > 100 * 1024 * 1024:
                        files.append((size, fp))
                except:
                    pass
        files.sort(reverse=True)
        print(f"找到 {len(files)} 个大文件 (>100MB):")
        for size, fp in files[:20]:
            print(f"  {size/1024**3:.2f}GB {fp[:80]}")

    elif cmd == "find2":
        if len(args) < 2:
            print("用法: devtools find2 <目录> <文件名模式>")
            return
        path = os.path.expanduser(args[0])
        pattern = args[1]
        results = glob.glob(os.path.join(path, '**', pattern), recursive=True)
        print(f"🔍 找到 {len(results)} 个匹配:")
        for r in results[:30]:
            print(f"  {r}")

    elif cmd == "size":
        if not args:
            print("用法: devtools size <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        size = os.path.getsize(filepath)
        print(f"📊 文件: {filepath}")
        print(f"   大小: {size:,} bytes")
        if size > 1024**3:
            print(f"        {size/1024**3:.2f} GB")
        elif size > 1024**2:
            print(f"        {size/1024**2:.2f} MB")
        elif size > 1024:
            print(f"        {size/1024:.2f} KB")

    elif cmd == "wc":
        if not args:
            print("用法: devtools wc <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        with open(filepath, 'r', errors='ignore') as f:
            lines = f.readlines()
        chars = sum(len(l) for l in lines)
        words = sum(len(l.split()) for l in lines)
        print(f"📊 统计: {filepath}")
        print(f"   行数: {len(lines):,}")
        print(f"   单词: {words:,}")
        print(f"   字符: {chars:,}")

    elif cmd == "lines":
        if not args:
            print("用法: devtools lines <文件路径> [起始行] [行数]")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        start = int(args[1]) - 1 if len(args) > 1 else 0
        count = int(args[2]) if len(args) > 2 else 50
        with open(filepath, 'r', errors='ignore') as f:
            lines = f.readlines()
        for i, line in enumerate(lines[start:start+count], start+1):
            print(f"{i:6d}  {line}", end='')

    elif cmd == "cat":
        if not args:
            print("用法: devtools cat <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        with open(filepath, 'r', errors='ignore') as f:
            print(f.read()[:2000])

    elif cmd == "hash":
        if not args:
            print("用法: devtools hash <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        print(f"🔐 计算哈希: {filepath}")
        with open(filepath, 'rb') as f:
            data = f.read()
        print(f"MD5:    {hashlib.md5(data).hexdigest()}")
        print(f"SHA1:   {hashlib.sha1(data).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(data).hexdigest()}")

    elif cmd == "md5":
        if not args:
            print("用法: devtools md5 <文件路径或字符串>")
            return
        text = args[0]
        if os.path.exists(os.path.expanduser(text)):
            with open(os.path.expanduser(text), 'rb') as f:
                text = f.read()
            print(f"MD5: {hashlib.md5(text).hexdigest()}")
        else:
            print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")

    elif cmd == "sha1":
        if not args:
            print("用法: devtools sha1 <文件路径或字符串>")
            return
        text = args[0]
        if os.path.exists(os.path.expanduser(text)):
            with open(os.path.expanduser(text), 'rb') as f:
                text = f.read()
            print(f"SHA1: {hashlib.sha1(text).hexdigest()}")
        else:
            print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")

    elif cmd == "sha256":
        if not args:
            print("用法: devtools sha256 <文件路径或字符串>")
            return
        text = args[0]
        if os.path.exists(os.path.expanduser(text)):
            with open(os.path.expanduser(text), 'rb') as f:
                text = f.read()
            print(f"SHA256: {hashlib.sha256(text).hexdigest()}")
        else:
            print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")

    elif cmd == "json":
        if not args:
            print("用法: devtools json <JSON字符串或文件路径>")
            return
        text = args[0]
        if os.path.exists(os.path.expanduser(text)):
            with open(os.path.expanduser(text)) as f:
                text = f.read()
        try:
            obj = json.loads(text)
            print(json.dumps(obj, indent=2, ensure_ascii=False))
        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析错误: {e}")

    elif cmd == "base64":
        if len(args) < 2:
            print("用法: devtools base64 <encode|decode> <文本或文件路径>")
            return
        mode = args[0]
        text = args[1]
        if os.path.exists(os.path.expanduser(text)):
            with open(os.path.expanduser(text), 'rb') as f:
                text = f.read()
                if mode == 'encode':
                    print(base64.b64encode(text).decode())
                elif mode == 'decode':
                    print(base64.b64decode(text).decode(errors='ignore'))
        else:
            text = text.encode()
            if mode == 'encode':
                print(base64.b64encode(text).decode())
            elif mode == 'decode':
                try:
                    print(base64.b64decode(text).decode(errors='ignore'))
                except:
                    print("❌ 解码失败")

    elif cmd == "url":
        if len(args) < 2:
            print("用法: devtools url <encode|decode> <URL>")
            return
        mode = args[0]
        text = ' '.join(args[1:])
        if mode == 'encode':
            print(urllib.parse.quote(text))
        elif mode == 'decode':
            print(urllib.parse.unquote(text))

    elif cmd == "env":
        if args:
            key = args[0]
            print(f"{key}={os.environ.get(key, '❌ 未设置')}")
        else:
            print("🔧 环境变量:")
            for k, v in sorted(os.environ.items()):
                print(f"  {k}={v}")

    elif cmd == "tree":
        if not args:
            path = os.path.expanduser('.')
        else:
            path = os.path.expanduser(args[0])
        max_depth = 3
        if len(args) > 1:
            try:
                max_depth = int(args[1])
            except:
                pass
        
        def print_tree(p, prefix="", depth=0):
            if depth >= max_depth:
                return
            try:
                items = sorted(os.listdir(p))
                dirs = [i for i in items if os.path.isdir(os.path.join(p, i)) and not i.startswith('.')]
                files = [i for i in items if os.path.isfile(os.path.join(p, i)) and not i.startswith('.')]
                
                for d in dirs[:10]:
                    print(f"{prefix}📁 {d}/")
                    print_tree(os.path.join(p, d), prefix + "   ", depth + 1)
                for f in files[:10]:
                    print(f"{prefix}📄 {f}")
            except PermissionError:
                pass
        
        print(f"🌳 目录树: {path}")
        print_tree(path)

    elif cmd == "preview":
        if not args:
            print("用法: devtools preview <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            return
        size = os.path.getsize(filepath)
        if size > 1024 * 100:
            print(f"📄 预览（仅显示前10KB）:")
            with open(filepath, 'r', errors='ignore') as f:
                print(f.read(10240))
        else:
            print(f"📄 预览:")
            with open(filepath, 'r', errors='ignore') as f:
                print(f.read())

    elif cmd == "compare":
        if len(args) < 2:
            print("用法: devtools compare <文件1> <文件2>")
            return
        f1 = os.path.expanduser(args[0])
        f2 = os.path.expanduser(args[1])
        if not os.path.exists(f1) or not os.path.exists(f2):
            print("❌ 文件不存在")
            return
        with open(f1, 'rb') as a, open(f2, 'rb') as b:
            hash1 = hashlib.md5(a.read()).hexdigest()
            hash2 = hashlib.md5(b.read()).hexdigest()
        if hash1 == hash2:
            print("✅ 文件相同")
        else:
            print("❌ 文件不同")
            print(f"  {args[0]}: {hash1}")
            print(f"  {args[1]}: {hash2}")

    elif cmd == "diff":
        if len(args) < 2:
            print("用法: devtools diff <文件1> <文件2>")
            return
        os.system(f'diff "{args[0]}" "{args[1]}"')

    elif cmd == "mime":
        if not args:
            print("用法: devtools mime <文件路径>")
            return
        filepath = os.path.expanduser(args[0])
        import mimetypes
        mime_type, _ = mimetypes.guess_type(filepath)
        print(f"📋 文件类型: {mime_type or '未知'}")
        if os.path.isdir(filepath):
            print(f"   类型: 目录")
        elif os.path.isfile(filepath):
            print(f"   大小: {os.path.getsize(filepath):,} bytes")

    elif cmd == "grep":
        if len(args) < 2:
            print("用法: devtools grep <模式> <文件>")
            return
        pattern = args[0]
        filepath = os.path.expanduser(args[1])
        try:
            with open(filepath, 'r', errors='ignore') as f:
                for i, line in enumerate(f, 1):
                    if re.search(pattern, line):
                        print(f"{i:6d}: {line}", end='')
        except Exception as e:
            print(f"❌ 搜索失败: {e}")

    # ========== 开发工具 ==========
    elif cmd == "ports":
        from devtools_hub.scanner import scan_common_ports
        print("🔍 扫描常用端口...")
        ports = scan_common_ports()
        if ports:
            for p in ports:
                print(f"  ✅ {p['port']} ({p['name']}) - 开放")
        else:
            print("  未发现开放端口")

    elif cmd == "services":
        from devtools_hub.scanner import get_services
        print("📋 系统服务:")
        services = get_services()
        for s in services[:20]:
            pid_str = str(s['pid']) if s['pid'] else '-'
            print(f"  [{pid_str:>6}] {s['name']}")

    elif cmd == "git":
        os.system('git status')

    elif cmd == "gstatus":
        os.system('gitstatus')
        os.system('git status')

    elif cmd == "glog":
        os.system('git log --oneline -20')

    elif cmd == "gbranch":
        os.system('git branch -a')

    elif cmd == "gpull":
        os.system('git pull')

    elif cmd == "gpush":
        os.system('git push')

    elif cmd == "node":
        os.system('node --version 2>/dev/null || echo "Node.js 未安装"')
        os.system('npm --version 2>/dev/null || echo "npm 未安装"')

    elif cmd == "python":
        v = sys.version_info
        print(f"Python: {v.major}.{v.minor}.{v.micro}")
        try:
            import pip
            print(f"pip: {pip.__version__}")
        except:
            pass

    elif cmd == "which":
        if not args:
            print("用法: devtools which <命令>")
            return
        cmd_name = args[0]
        path = shutil.which(cmd_name)
        if path:
            print(f"✅ {cmd_name} → {path}")
        else:
            print(f"❌ 未找到: {cmd_name}")

    elif cmd == "npm":
        if args and args[0] == 'list':
            os.system('npm list -g --depth=0')
        elif args and args[0] == 'outdated':
            os.system('npm outdated -g')
        else:
            os.system('npm --version')

    elif cmd == "pip3":
        if args and args[0] == 'list':
            os.system(f'{sys.executable} -m pip list')
        elif args and args[0] == 'outdated':
            os.system(f'{sys.executable} -m pip list --outdated')
        elif args and args[0] == 'freeze':
            os.system(f'{sys.executable} -m pip freeze')
        else:
            os.system(f'{sys.executable} -m pip --version')

    elif cmd == "brew":
        if args and args[0] == 'list':
            os.system('brew list')
        elif args and args[0] == 'outdated':
            os.system('brew outdated')
        elif args and args[0] == 'cleanup':
            os.system('brew cleanup')
        else:
            os.system('brew --version')

    elif cmd == "docker":
        os.system('docker ps -a')

    elif cmd == "dlog":
        if not args:
            print("用法: devtools dlog <容器名>")
            return
        os.system(f'docker logs --tail 50 {args[0]}')

    elif cmd == "gh":
        os.system('gh --version')

    elif cmd == "code":
        if args:
            os.system(f'code {" ".join(args)}')
        else:
            print("用法: devtools code <文件或目录>")

    # ========== 系统工具 ==========
    elif cmd == "info":
        print(f"""
🖥️  系统信息:
  系统: {platform.system()} {platform.release()} {platform.machine()}
  主机: {platform.node()}
  处理器: {platform.processor()}
  Python: {platform.python_version()}
  macOS: {platform.mac_ver()[0]}
""")

    elif cmd == "bench":
        if check():
            r = requests.get(f"{URL}/api/benchmark/full")
            print(json.dumps(r.json(), indent=2))
        else:
            print("❌ 服务未运行，请先 devtools start")
            print("💡 或直接运行: devtools cpu")

    elif cmd == "clean":
        print("🧹 清理缓存...")
        dirs = [
            '~/Library/Caches/com.apple.nsurlsessiond',
            '~/.cache',
        ]
        cleaned = 0
        for d in dirs:
            path = os.path.expanduser(d)
            if os.path.exists(path):
                size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(path) for f in fs)
                cleaned += size
                print(f"  清理: {d} ({size/1024**2:.1f}MB)")
        print(f"✅ 可释放: {cleaned/1024**2:.1f}MB（手动清理更彻底）")
        print("💡 提示: 使用 'sudo periodic daily weekly monthly' 清理系统缓存")

    elif cmd == "update":
        print("🔄 检查更新...")
        import importlib.metadata as metadata
        try:
            current_version = metadata.version('devtools-hub')
        except:
            current_version = '3.0.0'
        try:
            req = urllib.request.urlopen('https://pypi.org/pypi/devtools-hub/json', timeout=5)
            data = json.loads(req.read())
            latest_version = data['info']['version']
            print(f"当前版本: {current_version}")
            print(f"PyPI 最新版本: {latest_version}")
            if latest_version != current_version:
                print(f"📦 发现新版本 {latest_version}，正在更新...")
                os.system(f'{sys.executable} -m pip install --upgrade devtools-hub')
                print("✅ 更新成功！")
                print("💡 运行 'source ~/.zshrc' 使 PATH 生效")
            else:
                print("✅ 已是最新版本")
        except Exception as e:
            print(f"❌ 检查失败: {e}")

    elif cmd == "selfupdate":
        print("🔄 正在自更新 devtools-hub...")
        os.system(f'{sys.executable} -m pip install --upgrade --force-reinstall devtools-hub')
        print("💡 运行 'source ~/.zshrc' 使 PATH 生效")

    elif cmd == "start":
        print("🚀 启动服务...")
        os.system(f'{sys.executable} -m devtools_hub.server &')
        time.sleep(2)
        print(f"✅ 已启动: {URL}")

    elif cmd == "stop":
        os.system("pkill -f 'devtools_hub.server'")
        print("✅ 已停止")

    elif cmd == "date":
        now = datetime.datetime.now()
        print(f"📅 {now.strftime('%Y-%m-%d %A')}")
        print(f"🕐 {now.strftime('%H:%M:%S')}")
        print(f"📅 ISO: {now.isoformat()}")

    elif cmd == "cal":
        os.system('cal')

    elif cmd == "who":
        os.system('who')

    elif cmd == "history":
        hist_file = os.path.expanduser('~/.zsh_history')
        if os.path.exists(hist_file):
            with open(hist_file, 'r') as f:
                lines = f.readlines()
            print(f"📜 最近命令历史 ({len(lines)} 条):")
            for line in lines[-30:]:
                cmd_hist = line.strip().split(';')[-1].strip()
                if cmd_hist:
                    print(f"  {cmd_hist}")
        else:
            print("❌ 未找到历史记录")

    elif cmd == "aliases":
        print("🔤 所有别名:")
        for k, v in sorted(os.environ.items()):
            if 'alias' in k.lower():
                print(f"  {k}={v}")

    elif cmd == "pwd":
        print(os.getcwd())

    elif cmd == "cd":
        if args:
            path = os.path.expanduser(args[0])
            os.chdir(path)
        print(os.getcwd())

    elif cmd == "ls":
        path = os.getcwd() if not args else os.path.expanduser(args[0])
        items = sorted(os.listdir(path))
        for item in items:
            if not item.startswith('.'):
                full = os.path.join(path, item)
                if os.path.isdir(full):
                    print(f"📁 {item}/")
                else:
                    size = os.path.getsize(full)
                    size_str = f"{size:,}" if size < 1024*1024 else f"{size/1024:.1f}KB"
                    print(f"📄 {item} ({size_str})")

    elif cmd == "open":
        if not args:
            print("用法: devtools open <文件或URL>")
            return
        os.system(f'open "{args[0]}"')

    elif cmd == "run":
        if not args:
            print("用法: devtools run <脚本路径>")
            return
        filepath = os.path.expanduser(args[0])
        if filepath.endswith('.py'):
            os.system(f'{sys.executable} "{filepath}"')
        elif filepath.endswith('.sh'):
            os.system(f'bash "{filepath}"')
        else:
            os.system(f'"{filepath}"')

    # ========== 剪贴板 & 截图 ==========
    elif cmd == "clip":
        try:
            content = subprocess.run(['pbpaste'], capture_output=True, text=True).stdout
            print(f"📋 剪贴板内容:\n{content[:500]}")
        except:
            print("❌ 无法获取剪贴板")

    elif cmd == "clips":
        if not args:
            print("用法: devtools clips <文本>")
            return
        text = ' '.join(args)
        try:
            subprocess.run(['pbcopy'], input=text.encode(), check=True)
            print(f"✅ 已复制到剪贴板: {text[:50]}...")
        except:
            print("❌ 无法复制到剪贴板")

    elif cmd == "screenshot":
        print("📸 截图...")
        Desktop = os.path.expanduser("~/Desktop")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{Desktop}/screenshot_{timestamp}.png"
        os.system(f'screencapture -x "{filename}"')
        print(f"✅ 已保存: {filename}")

    elif cmd == "record":
        print("🎬 开始屏幕录制 (Ctrl+C 停止)...")
        Desktop = os.path.expanduser("~/Desktop")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{Desktop}/recording_{timestamp}.mov"
        os.system(f'screencapture -v "{filename}"')
        print(f"✅ 已保存: {filename}")

    # ========== 通知 & 提醒 ==========
    elif cmd == "notify":
        if not args:
            print("用法: devtools notify <消息>")
            return
        message = ' '.join(args)
        try:
            os.system(f'terminal-notifier -message "{message}" -title "DevTools"')
            print(f"✅ 通知已发送: {message}")
        except:
            print("❌ 通知发送失败（需要 terminal-notifier）")

    elif cmd == "remind":
        if len(args) < 2:
            print("用法: devtools remind <分钟> <消息>")
            return
        mins = int(args[0])
        message = ' '.join(args[1:])
        print(f"⏰ {mins}分钟后提醒: {message}")
        time.sleep(mins * 60)
        try:
            os.system(f'terminal-notifier -message "{message}" -title "提醒"')
        except:
            pass

    elif cmd == "timer":
        if not args:
            print("用法: devtools timer <秒数>")
            return
        secs = int(args[0])
        print(f"⏱️ 计时器: {secs} 秒")
        for i in range(secs, 0, -1):
            print(f"\r{i}", end='', flush=True)
            time.sleep(1)
        print("\n🔔 时间到！")
        os.system('say "时间到"')

    elif cmd == "stopwatch":
        print("⏱️ 秒表 (Ctrl+C 停止)")
        start = time.time()
        try:
            while True:
                elapsed = time.time() - start
                print(f"\r{elapsed:.2f}秒", end='', flush=True)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n✅ 总计: {elapsed:.2f}秒")

    # ========== 工具箱 ==========
    elif cmd == "uuid":
        print(f"🆔 UUID: {uuid.uuid4()}")

    elif cmd == "password":
        length = int(args[0]) if args and args[0].isdigit() else 16
        chars = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(secrets.choice(chars) for _ in range(length))
        print(f"🔐 密码: {pwd}")

    elif cmd == "rand":
        if args:
            max_num = int(args[0])
        else:
            max_num = 100
        print(f"🎲 随机数 (1-{max_num}): {secrets.randbelow(max_num) + 1}")

    elif cmd == "hex":
        if not args:
            print("用法: devtools hex <数字或字符串>")
            return
        text = args[0]
        try:
            num = int(text)
            print(f"HEX: {hex(num)}")
        except:
            print(f"HEX: {text.encode().hex()}")

    elif cmd == "ascii":
        if not args:
            print("用法: devtools ascii <字符>")
            return
        char = args[0][0]
        print(f"ASCII: {ord(char)} (0x{ord(char):02X})")

    elif cmd == "epoch":
        if args:
            ts = int(args[0])
            dt = datetime.datetime.fromtimestamp(ts)
            print(f"📅 {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("用法: devtools epoch <时间戳>")

    elif cmd == "now":
        print(f"🕐 当前时间戳: {int(time.time())}")
        print(f"📅 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    elif cmd == "encode":
        if not args:
            print("用法: devtools encode <文本>")
            return
        text = ' '.join(args)
        encodings = ['utf-8', 'gbk', 'gb2312', 'big5', 'shift_jis']
        print(f"🔍 编码检测: {text[:50]}")
        for enc in encodings:
            try:
                text.encode(enc)
                print(f"  ✅ {enc}")
            except:
                print(f"  ❌ {enc}")

    elif cmd == "compress":
        if not args:
            print("用法: devtools compress <文本>")
            return
        text = ' '.join(args).encode()
        compressed = zlib.compress(text)
        print(f"📦 原始大小: {len(text)} bytes")
        print(f"📦 压缩后: {len(compressed)} bytes")
        print(f"📦 压缩率: {(1-len(compressed)/len(text))*100:.1f}%")

    # ========== macOS 设置 ==========
    elif cmd == "volume":
        if args:
            vol = args[0]
            os.system(f'osascript -e "set volume output volume {vol}"')
            print(f"✅ 音量设置为 {vol}%")
        else:
            os.system('osascript -e "output volume of (get volume settings)"')

    elif cmd == "mute":
        os.system('osascript -e "set volume output muted not (output muted of (get volume settings))"')
        print("🔇 静音切换")

    elif cmd == "brightness":
        if not args:
            print("用法: devtools brightness <0-100>")
            return
        brightness = int(args[0])
        os.system(f'display brightness -d {brightness/100}')
        print(f"✅ 亮度设置为 {brightness}%")

    elif cmd == "theme":
        mode = args[0] if args else 'auto'
        if mode == 'dark':
            os.system('defaults write NSGlobalDomain AppleInterfaceStyle -string Dark')
            print("✅ 已切换到深色模式")
        elif mode == 'light':
            os.system('defaults delete NSGlobalDomain AppleInterfaceStyle')
            print("✅ 已切换到浅色模式")
        else:
            print("用法: devtools theme <dark|light>")

    elif cmd == "nightshift":
        state = subprocess.run(['defaults', 'read', 'domain', 'kUnifiedScaleFactorPrefs'], capture_output=True).returncode
        if state == 0:
            print("✅ 夜览模式已开启")
        else:
            print("❌ 夜览模式未开启")

    elif cmd == "dnd":
        os.system('defaults -currentHost write com.apple.notificationcenterui doNotDisturb -bool true')
        os.system('killall NotificationCenter')
        print("✅ 勿扰模式已开启")

    # ========== 安装 & 服务 ==========
    elif cmd == "install":
        if not args:
            print("用法: devtools install <应用名>")
            return
        os.system(f'homebrew install {args[0]}')

    elif cmd == "uninstall":
        if not args:
            print("用法: devtools uninstall <应用名>")
            return
        os.system(f'homebrew uninstall {args[0]}')

    elif cmd == "running":
        print("📋 正在运行的应用:")
        try:
            apps = subprocess.run(['osascript', '-e', 'tell application "System Events" to get name of (processes where background only is false)'], capture_output=True, text=True).stdout
            for app in apps.strip().split(', '):
                print(f"  📎 {app}")
        except:
            print("❌ 无法获取应用列表")

    elif cmd == "processes":
        os.system('launchctl list | grep -v "^-"')

    elif cmd == "curl":
        url = args[0] if args else input("URL: ")
        method = args[1].upper() if len(args) > 1 else "GET"
        try:
            r = requests.request(method, url, timeout=10)
            print(f"📊 Status: {r.status_code}")
            print(f"📏 Size: {len(r.content)} bytes")
            print(f"\n{r.text[:2000]}")
        except ImportError:
            os.system(f'curl -s "{url}" | head -50')
        except:
            print("❌ 请求失败")

    elif cmd == "headers":
        url = args[0] if args else input("URL: ")
        try:
            r = requests.head(url, timeout=10)
            for k, v in r.headers.items():
                print(f"  {k}: {v}")
        except:
            print("❌ 获取失败")

    elif cmd == "dns":
        domain = args[0] if args else input("域名: ")
        try:
            addrs = socket.getaddrinfo(domain, 80)
            for a in addrs:
                print(f"  {a[4][0]} ({a[0].name})")
        except:
            os.system(f'dig {domain} +short')

    elif cmd == "ping":
        host = args[0] if args else "8.8.8.8"
        count = args[1] if len(args) > 1 else "4"
        os.system(f'ping -c {count} {host}')

    elif cmd == "scan":
        if not args:
            print("用法: devtools scan <host> [端口]")
            return
        host = args[0]
        ports = args[1] if len(args) > 1 else "80,443,22,3389,3306,5432,6379,27017"
        for port in ports.split(','):
            try:
                s = socket.socket()
                s.settimeout(1)
                result = s.connect_ex((host, int(port)))
                if result == 0:
                    print(f"  ✅ {port} 开放")
                s.close()
            except:
                pass

    elif cmd == "uuid":
        count = int(args[0]) if args and args[0].isdigit() else 1
        for i in range(count):
            print(uuid.uuid4())

    elif cmd == "password":
        import secrets
        length = int(args[0]) if args and args[0].isdigit() else 16
        chars = args[1] if len(args) > 1 else "alphanumeric"
        if chars == "alphanumeric":
            print(secrets.token_urlsafe(length))
        elif chars == "hex":
            print(secrets.token_hex(length))
        elif chars == "ascii":
            print(secrets.token_urlsafe(length))

    elif cmd == "base64enc":
        text = ' '.join(args) if args else sys.stdin.read().strip()
        import base64
        print(base64.b64encode(text.encode()).decode())

    elif cmd == "base64dec":
        text = ' '.join(args) if args else sys.stdin.read().strip()
        import base64
        try:
            print(base64.b64decode(text).decode())
        except:
            print("❌ 解码失败")

    elif cmd == "hex":
        text = ' '.join(args) if args else input("文本转HEX: ")
        print(text.encode().hex())

    elif cmd == "unhex":
        text = ' '.join(args) if args else input("HEX转文本: ")
        print(bytes.fromhex(text).decode())

    elif cmd == "md5":
        data = ' '.join(args) if args else input("MD5: ")
        print(hashlib.md5(data.encode()).hexdigest())

    elif cmd == "sha256":
        data = ' '.join(args) if args else input("SHA256: ")
        print(hashlib.sha256(data.encode()).hexdigest())

    elif cmd == "tree":
        path = os.path.expanduser(args[0]) if args else "."
        max_depth = int(args[1]) if len(args) > 1 else 3
        def show_tree(p, prefix="", depth=0):
            if depth >= max_depth:
                return
            try:
                items = sorted(os.listdir(p))
                dirs = [i for i in items if os.path.isdir(os.path.join(p, i))]
                files = [i for i in items if os.path.isfile(os.path.join(p, i))]
                for f in files:
                    print(f"{prefix}├── 📄 {f}")
                for d in dirs:
                    print(f"{prefix}├── 📁 {d}/")
                    show_tree(os.path.join(p, d), prefix + "│   ", depth + 1)
            except:
                pass
        print(f"📁 {path}/")
        show_tree(path)

    elif cmd == "find":
        if len(args) < 2:
            print("用法: devtools find <目录> <关键字>")
            return
        path = os.path.expanduser(args[0])
        keyword = args[1]
        result = subprocess.run(['find', path, '-name', f'*{keyword}*', '-type', 'f'], 
                              capture_output=True, text=True)
        print(result.stdout or "(未找到)")

    elif cmd == "grep":
        if len(args) < 2:
            print("用法: devtools grep <文件> <关键字>")
            return
        path = os.path.expanduser(args[0])
        keyword = args[1]
        result = subprocess.run(['grep', '-n', keyword, path], 
                              capture_output=True, text=True)
        print(result.stdout or "(未找到)")

    elif cmd == "size":
        path = os.path.expanduser(args[0]) if args else "."
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total += os.path.getsize(fp)
                except:
                    pass
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if total < 1024:
                print(f"📦 {total:.2f} {unit}")
                break
            total /= 1024

    elif cmd == "cleanup":
        paths = [
            os.path.expanduser("~/Library/Logs"),
            "/tmp",
            "/var/tmp"
        ]
        for p in paths:
            if os.path.exists(p):
                result = subprocess.run(['du', '-sh', p], capture_output=True, text=True)
                print(f"  {p}: {result.stdout.strip()}")
        print("💡 使用 'brew cleanup' 清理 Homebrew 缓存")

    elif cmd == "service":
        action = args[0] if args else "status"
        name = args[1] if len(args) > 1 else "mysql"
        if action == "start":
            os.system(f'sudo launchctl load /Library/LaunchDaemons/{name}.plist')
        elif action == "stop":
            os.system(f'sudo launchctl unload /Library/LaunchDaemons/{name}.plist')
        elif action == "status":
            os.system(f'launchctl list | grep {name}')
        else:
            print(f"用法: service <start|stop|status> <服务名>")

    elif cmd == "cron":
        if len(args) < 2:
            print("用法: cron <add|remove|list> <规则>")
            print("示例: cron add '*/5 * * * *' 'echo hello'")
            return
        action, rule = args[0], args[1]
        if action == "add":
            cmd_str = ' '.join(args[2:]) if len(args) > 2 else input("命令: ")
            cron = f"{rule} {cmd_str}"
            subprocess.run(f'(crontab -l; echo "{cron}") | crontab -', shell=True)
            print("✅ 已添加")
        elif action == "remove":
            subprocess.run('crontab -r', shell=True)
            print("✅ 已清除")
        else:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            print(result.stdout or "(无任务)")

    elif cmd == "git":
        subcmd = args[0] if args else "status"
        os.system(f'git {subcmd}')

    elif cmd == "github":
        repo = args[0] if args else ""
        if not repo:
            print("用法: github <用户名/仓库>")
            return
        try:
            r = requests.get(f'https://api.github.com/repos/{repo}', timeout=10)
            if r.status_code == 200:
                data = r.json()
                print(f"📦 {data['full_name']}")
                print(f"⭐ {data['stargazers_count']} | 🍴 {data['forks_count']}")
                print(f"📝 {data['description']}")
                print(f"🔗 {data['html_url']}")
            else:
                print("❌ 仓库不存在")
        except:
            print("❌ 网络错误")

    elif cmd == "pypi":
        package = args[0] if args else ""
        if not package:
            print("用法: pypi <包名>")
            return
        try:
            r = requests.get(f'https://pypi.org/pypi/{package}/json', timeout=10)
            if r.status_code == 200:
                data = r.json()
                print(f"📦 {data['info']['name']} v{data['info']['version']}")
                print(f"📝 {data['info']['summary']}")
                print(f"🔗 https://pypi.org/project/{package}/")
            else:
                print("❌ 包不存在")
        except:
            print("❌ 网络错误")

    elif cmd == "now":
        now = datetime.datetime.now()
        print(f"🕐 {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📅 {now.strftime('%A, %B %d, %Y')}")
        print(f"⏱️  时间戳: {int(now.timestamp())}")

    elif cmd == "dateconv":
        if not args:
            print("用法: dateconv <时间戳或日期>")
            print("示例: dateconv 1712505600")
            print("示例: dateconv 2024-04-08")
            return
        try:
            ts = int(args[0])
            print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        except:
            try:
                dt = datetime.datetime.strptime(args[0], '%Y-%m-%d')
                print(f"时间戳: {int(dt.timestamp())}")
            except:
                print("❌ 格式错误")

    elif cmd == "timeconv":
        if len(args) < 2:
            print("用法: timeconv <时间> <源时区> <目标时区>")
            return
        time_str, from_tz, to_tz = args[0], args[1], args[2]
        print(f"🕐 {time_str} ({from_tz} → {to_tz})")
        # 简单实现，显示 UTC 时间
        print("💡 建议使用: date -j -f '%Y-%m-%d %H:%M'")

    elif cmd == "todo":
        path = os.path.expanduser("~/.devtools_todo.txt")
        if not args:
            if os.path.exists(path):
                with open(path) as f:
                    for i, line in enumerate(f, 1):
                        print(f"  {i}. {line.strip()}")
            else:
                print("(无待办事项)")
        elif args[0] == "add":
            item = ' '.join(args[1:])
            with open(path, 'a') as f:
                f.write(f"{item}\n")
            print("✅ 已添加")
        elif args[0] == "clear":
            if os.path.exists(path):
                os.remove(path)
            print("✅ 已清空")
        else:
            print(f"  📝 {args[0]}")

    elif cmd == "note":
        path = os.path.expanduser("~/.devtools_notes.txt")
        if not args:
            if os.path.exists(path):
                with open(path) as f:
                    print(f.read())
        else:
            with open(path, 'a') as f:
                f.write(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] ")
                f.write(' '.join(args) + "\n")
            print("✅ 已保存")

    elif cmd == "cheatsheet":
        sheets = {
            'git': "git status | git add . | git commit -m | git push",
            'docker': "docker ps | docker images | docker build | docker run",
            'ssh': "ssh user@host | ssh -i key user@host | ssh-copy-id user@host",
            'vim': "i插入 | esc退出 | :wq保存 | :q!强制退出 | dd删除行",
            'tmux': "Ctrl+b c新建 | Ctrl+b d分离 | tmux attach恢复",
        }
        if args:
            key = args[0]
            print(sheets.get(key, "(未找到速查表)"))
        else:
            for k, v in sheets.items():
                print(f"📋 {k}: {v}")

    elif cmd == "snippet":
        snippets = {
            'http': 'python3 -m http.server 8080',
            'json': 'cat file.json | python3 -m json.tool',
            'port': 'lsof -i :PORT',
            'kill': 'kill -9 PID',
            'gitlog': 'git log --oneline -10',
        }
        name = args[0] if args else ""
        if name and name in snippets:
            print(snippets[name])
            import subprocess
            subprocess.run('pbcopy', input=snippets[name].encode())
            print("✅ 已复制到剪贴板")
        else:
            for k, v in snippets.items():
                print(f"  {k}: {v}")

    elif cmd == "cheat":
        # 快速命令速查
        shortcuts = {
            's': 'devtools status',
            'c': 'devtools cpu',
            'm': 'devtools mem',
            'd': 'devtools disk',
            'p': 'devtools ports',
            'i': 'devtools ip',
            'k': 'devtools killport',
            'w': 'devtools weather',
            'ip': 'devtools myip',
            'calc': 'devtools calc',
        }
        if args:
            key = args[0]
            print(f"📝 {shortcuts.get(key, key)}")
        else:
            print("💡 快捷命令速查:")
            for k, v in shortcuts.items():
                print(f"  {k} → {v}")

    elif cmd == "dockerps":
        os.system('docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"')

    elif cmd == "dockerlogs":
        container = args[0] if args else input("容器名: ")
        lines = args[1] if len(args) > 1 else "50"
        os.system(f'docker logs --tail {lines} {container}')

    elif cmd == "dockerexec":
        if len(args) < 2:
            print("用法: dockerexec <容器> <命令>")
            return
        os.system(f'docker exec -it {args[0]} {args[1]}')

    elif cmd == "npm":
        subcmd = args[0] if args else "list"
        os.system(f'npm {subcmd}')

    elif cmd == "pip":
        subcmd = args[0] if args else "list"
        os.system(f'pip3 {subcmd}')

    elif cmd == "brew":
        subcmd = args[0] if args else "list"
        os.system(f'brew {subcmd}')

    elif cmd == "sysinfo":
        import platform
        print(f"🖥️  {platform.node()}")
        print(f"   系统: {platform.system()} {platform.release()}")
        print(f"   版本: {platform.version()}")
        print(f"   架构: {platform.machine()}")
        print(f"   Python: {platform.python_version()}")

    elif cmd == "battery":
        try:
            result = subprocess.run(['pmset', '-g', 'batt'], capture_output=True, text=True)
            print(result.stdout)
        except:
            print("❌ 无法获取电池信息")

    elif cmd == "wifi":
        result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], capture_output=True, text=True)
        print(f"📶 当前WiFi: {result.stdout.strip()}")
        # 附近网络
        os.system('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport scan | head -20')

    elif cmd == "openurl":
        url = args[0] if args else input("URL: ")
        os.system(f'open "{url}"')

    elif cmd == "kill":
        if not args:
            print("用法: devtools kill <进程名或PID>")
            return
        pid = args[0]
        if pid.isdigit():
            os.system(f'kill -9 {pid}')
        else:
            result = subprocess.run(['pkill', '-9', pid], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ 已终止: {pid}")
            else:
                print(f"❌ 进程不存在: {pid}")

    elif cmd == "restart":
        app = args[0] if args else input("应用名: ")
        os.system(f'osascript -e \'quit app "{app}"\' && sleep 1 && open -a "{app}"')
        print(f"✅ 已重启: {app}")

    elif cmd == "recent":
        count = int(args[0]) if args and args[0].isdigit() else 10
        result = subprocess.run(['ls', '-lt', os.path.expanduser('~/Downloads')], 
                              capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')[:count+1]
        for line in lines[1:]:
            print(line)

    elif cmd == "empty":
        folders = [
            "~/Downloads",
            "~/Desktop"
        ]
        for folder in folders:
            expanded = os.path.expanduser(folder)
            if os.path.exists(expanded):
                result = subprocess.run(['ls', '-A', expanded], capture_output=True, text=True)
                count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
                print(f"📁 {folder}: {count} 个文件")

    # ========== 实用工具 ==========
    elif cmd == "calc":
        expr = ' '.join(args) if args else input("计算: ")
        try:
            result = eval(expr, {"__builtins__": {}}, {})
            print(f"= {result}")
        except:
            print("❌ 表达式错误")

    elif cmd == "server":
        port = int(args[0]) if args else 8080
        folder = args[1] if len(args) > 1 else "."
        print(f"🚀 启动 HTTP 服务器: http://localhost:{port}")
        print(f"📁 目录: {os.path.abspath(folder)}")
        print(f"按 Ctrl+C 停止")
        os.system(f'cd "{os.path.abspath(folder)}" && python3 -m http.server {port}')

    elif cmd == "path":
        paths = os.environ.get('PATH', '').split(':')
        for i, p in enumerate(paths, 1):
            print(f"  {i}. {p}")

    elif cmd == "port":
        target = args[0] if args else ""
        if not target:
            print("用法: devtools port <端口号或关键字>")
            return
        result = subprocess.run(['lsof', '-i', f':{target}'], capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        else:
            print(f"❌ 端口 {target} 未被占用")

    elif cmd == "copy":
        text = ' '.join(args) if args else input("输入要复制的内容: ")
        subprocess.run('pbcopy', input=text.encode(), shell=False)
        print(f"✅ 已复制: {text[:50]}{'...' if len(text) > 50 else ''}")

    elif cmd == "paste":
        result = subprocess.run(['pbpaste'], capture_output=True)
        print(result.stdout.decode() or "(剪贴板为空)")

    elif cmd == "filesize":
        if not args:
            print("用法: devtools filesize <文件路径或大小(字节)>")
            return
        path = os.path.expanduser(args[0])
        if os.path.exists(path):
            size = os.path.getsize(path)
        else:
            try:
                size = int(args[0])
            except:
                print("❌ 无效输入")
                return
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                print(f"📦 {size:.2f} {unit}")
                break
            size /= 1024

    elif cmd == "qr":
        text = ' '.join(args) if args else input("输入二维码内容: ")
        try:
            import qrcode
            img = qrcode.make(text)
            path = os.path.expanduser("~/Desktop/qrcode.png")
            img.save(path)
            print(f"✅ 已保存: {path}")
            os.system(f'open "{path}"')
        except ImportError:
            print("❌ 需要安装 qrcode: pip3 install qrcode pillow")
            print(f"📝 内容: {text}")

    elif cmd == "jwt":
        token = args[0] if args else input("输入 JWT: ")
        try:
            parts = token.split('.')
            for i, part in enumerate(['Header', 'Payload', 'Signature']):
                print(f"\n📋 {part}:")
                import base64
                padded = part + '=' * (4 - len(part) % 4) if i < 2 else ''
                decoded = base64.urlsafe_b64decode(parts[i] + padded)
                print(json.dumps(json.loads(decoded), indent=2))
        except:
            print("❌ JWT 解析失败")

    elif cmd == "urldecode":
        text = ' '.join(args) if args else input("输入要解码的 URL: ")
        print(f"✅ {urllib.parse.unquote(text)}")

    elif cmd == "urlencode":
        text = ' '.join(args) if args else input("输入要编码的文本: ")
        print(f"✅ {urllib.parse.quote(text)}")

    elif cmd == "crontab":
        if args and args[0] == '-l':
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            print(result.stdout or "(无定时任务)")
        elif args and args[0] == '-r':
            subprocess.run(['crontab', '-r'])
            print("✅ 已清除所有定时任务")
        else:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            print(result.stdout or "(无定时任务)")

    elif cmd == "clipboard":
        if args and args[0] == 'history':
            print("📋 剪贴板历史 (最近10条):")
            try:
                import sqlite3
                db = subprocess.run(['sqlite3', os.path.expanduser('~/Library/Application Support/com.apple.Notes/Notes.sqlite'), 'SELECT ZTEXT FROM ZNOTEBODY'], capture_output=True, text=True)
                print(db.stdout[:500] or "(无历史)")
            except:
                print("(需要访问权限)")
        else:
            result = subprocess.run(['pbpaste'], capture_output=True)
            print(result.stdout.decode() or "(剪贴板为空)")

    elif cmd == "extract":
        if not args:
            print("用法: devtools extract <压缩文件>")
            return
        file = os.path.expanduser(args[0])
        import shutil
        if file.endswith('.zip'):
            shutil.unpack_archive(file, os.path.dirname(file))
        elif file.endswith(('.tar.gz', '.tgz')):
            shutil.unpack_archive(file, os.path.dirname(file))
        elif file.endswith('.tar'):
            shutil.unpack_archive(file, os.path.dirname(file))
        else:
            print("❌ 不支持的格式")
            return
        print(f"✅ 已解压: {file}")

    elif cmd == "download":
        if not args:
            print("用法: devtools download <URL>")
            return
        url = args[0]
        filename = args[1] if len(args) > 1 else os.path.basename(url)
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"✅ 已下载: {filename}")
        except Exception as e:
            print(f"❌ 下载失败: {e}")

    elif cmd == "whois":
        if not args:
            print("用法: devtools whois <域名>")
            return
        domain = args[0]
        os.system(f'whois {domain}')

    elif cmd == "myip":
        print("🌐 本机 IP 信息:")
        hostname = socket.gethostname()
        print(f"  主机名: {hostname}")
        print(f"  本地IP: {socket.gethostbyname(hostname)}")
        try:
            ip = urllib.request.urlopen('https://api.ipify.org', timeout=3).read().decode()
            print(f"  公网IP: {ip}")
        except:
            print("  公网IP: (获取失败)")

    elif cmd == "speedtest":
        print("📡 正在测速...")
        try:
            import speedtest
            s = speedtest.Speedtest()
            s.get_servers()
            s.get_best_server()
            download = s.download() / 1024 / 1024
            upload = s.upload() / 1024 / 1024
            print(f"⬇️ 下载: {download:.2f} Mbps")
            print(f"⬆️ 上传: {upload:.2f} Mbps")
        except ImportError:
            print("❌ 需要安装: pip3 install speedtest-cli")
        except:
            print("❌ 测速失败")

    elif cmd == "weather":
        if not args:
            city = "Shanghai"
        else:
            city = ' '.join(args)
        try:
            url = f"https://wttr.in/{city}?format=3"
            result = urllib.request.urlopen(url, timeout=3).read().decode()
            print(result)
        except:
            print("❌ 获取天气失败")

    elif cmd == "translate":
        if len(args) < 2:
            print("用法: devtools translate <中文或英文文本>")
            return
        text = ' '.join(args)
        try:
            r = requests.post('https://api.mymemory.translated.net/get', 
                            data={'q': text, 'langpair': 'zh|en' if '\u4e00' <= text[0] <= '\u9fff' else 'en|zh'},
                            timeout=5)
            result = r.json()
            print(f"📝 {result['responseData']['translatedText']}")
        except:
            print("❌ 翻译失败（需要网络）")

    elif cmd == "shorten":
        if not args:
            print("用法: devtools shorten <URL>")
            return
        url = args[0]
        try:
            r = requests.post('https://tinyurl.com/api-create.php', 
                            data={'url': url}, timeout=5)
            print(f"🔗 {r.text}")
        except:
            print("❌ 短链接生成失败")

    elif cmd == "hash":
        if len(args) < 2:
            print("用法: devtools hash <md5|sha1|sha256> <文本或文件>")
            return
        algo = args[0]
        data = args[1]
        if os.path.exists(os.path.expanduser(data)):
            with open(os.path.expanduser(data), 'rb') as f:
                content = f.read()
        else:
            content = data.encode()
        if algo == 'md5':
            print(f"MD5: {hashlib.md5(content).hexdigest()}")
        elif algo == 'sha1':
            print(f"SHA1: {hashlib.sha1(content).hexdigest()}")
        elif algo == 'sha256':
            print(f"SHA256: {hashlib.sha256(content).hexdigest()}")
        else:
            print("❌ 支持: md5, sha1, sha256")

    elif cmd == "random":
        if not args:
            import random
            print(f"🎲 随机数: {random.randint(1, 100)}")
        elif args[0] == 'str':
            length = int(args[1]) if len(args) > 1 else 16
            import secrets
            print(f"🔐 随机字符串: {secrets.token_urlsafe(length)}")
        elif args[0] == 'choice':
            items = args[1:]
            if items:
                import random
                print(f"🎯 随机选择: {random.choice(items)}")

    elif cmd == "timestamp":
        now = int(time.time())
        print(f"🕐 当前时间戳: {now}")
        dt = datetime.datetime.fromtimestamp(now)
        print(f"📅 转换日期: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        if args:
            try:
                ts = int(args[0])
                print(f"📅 时间戳 {ts}: {datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")
            except:
                pass

    elif cmd == "json":
        text = ' '.join(args) if args else sys.stdin.read()
        try:
            parsed = json.loads(text)
            print(json.dumps(parsed, indent=2, ensure_ascii=False))
        except:
            print("❌ JSON 解析失败")

    elif cmd == "jsonmin":
        text = ' '.join(args) if args else sys.stdin.read()
        try:
            parsed = json.loads(text)
            print(json.dumps(parsed, separators=(',', ':')))
        except:
            print("❌ JSON 解析失败")

    elif cmd == "gitlog":
        result = subprocess.run(['git', 'log', '--oneline', '-10'], capture_output=True, text=True)
        print(result.stdout or "(非 Git 仓库)")

    elif cmd == "gitdiff":
        result = subprocess.run(['git', 'diff', '--stat'], capture_output=True, text=True)
        print(result.stdout or "(无更改)")

    elif cmd == "gitsync":
        branch = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True).stdout.strip()
        print(f"🔄 同步分支: {branch}")
        subprocess.run(['git', 'fetch', 'origin'])
        subprocess.run(['git', 'reset', '--hard', f'origin/{branch}'])
        print("✅ 已同步到远程最新")

    elif cmd == "emoji":
        if not args:
            emojis = {
                'smile': '😄', 'laugh': '😂', 'love': '❤️', 
                'fire': '🔥', 'star': '⭐', 'rocket': '🚀',
                'check': '✅', 'x': '❌', 'warning': '⚠️',
                'info': 'ℹ️', 'clock': '⏰', 'calendar': '📅'
            }
            for k, v in emojis.items():
                print(f"  {k}: {v}")
        else:
            keyword = args[0].lower()
            matches = {
                'thumbsup': '👍', 'thumbsdown': '👎', 'ok': '👌',
                'wave': '👋', 'pray': '🙏', 'clap': '👏',
                '100': '💯', 'cool': '😎', 'thinking': '🤔'
            }
            print(matches.get(keyword, f"(未找到: {keyword})"))

    elif cmd == "color":
        if not args:
            print("用法: devtools color <#RRGGBB 或 颜色名>")
            print("示例: devtools color #ff0000")
            return
        color = args[0]
        if color.startswith('#'):
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            print(f"RGB: ({r}, {g}, {b})")
            # 简单判断亮暗
            luminance = (0.299*r + 0.587*g + 0.114*b) / 255
            print(f"亮度: {'亮色' if luminance > 0.5 else '暗色'}")

    elif cmd == "env":
        if args:
            key = args[0]
            print(os.environ.get(key, "(未设置)"))
        else:
            for k, v in sorted(os.environ.items()):
                print(f"  {k}={v}")

    elif cmd == "syslog":
        count = int(args[0]) if args and args[0].isdigit() else 20
        result = subprocess.run(['log', 'show', '--predicate', 'process == "kernel"', '--last', '1h', '-limit', str(count)],
                              capture_output=True, text=True)
        print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)

    elif cmd == "process":
        if not args:
            print("用法: devtools process <进程名>")
            return
        name = args[0]
        result = subprocess.run(['pgrep', '-a', name], capture_output=True, text=True)
        print(result.stdout or f"❌ 未找到进程: {name}")

    elif cmd == "killport":
        if not args:
            print("用法: devtools killport <端口>")
            return
        port = args[0]
        result = subprocess.run(['lsof', '-ti', f':{port}'], capture_output=True, text=True)
        if result.stdout:
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                subprocess.run(['kill', pid])
            print(f"✅ 已终止端口 {port} 上的进程")
        else:
            print(f"❌ 端口 {port} 未被占用")

    else:
        print(f"❌ 未知命令: {cmd}")
        print("💡 输入 'devtools' 查看所有命令")

if __name__ == "__main__":
    main()
