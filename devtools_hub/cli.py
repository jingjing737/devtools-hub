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
        import requests
        r = requests.get(f"{URL}/api/health", timeout=1)
        return r.ok
    except:
        return False

def main():
    if len(sys.argv) < 2:
        print("""
🔧 DevTools Hub v3.5.0 - 开发者工具集

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
""")
        return

    # ========== 参数解析 ==========
    if len(sys.argv) >= 2 and sys.argv[1] in ('-v', '--version'):
        print("v3.5.0")
        return
    elif len(sys.argv) >= 2 and sys.argv[1] in ('-h', '--help'):
        print("用法: devtools <命令>  或  dev <命令>")
        print("       devtools -v       或  dev -v")
        return
    else:
        cmd = sys.argv[1]
    args = sys.argv[2:]

    # ========== 系统监控 ==========
    if cmd == "status":
        if check():
            import requests
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
            import requests
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

    # ========== Git 增强 ==========
    elif cmd == "glog2":
        os.system('git log --oneline --graph --all -20')

    elif cmd == "gstash":
        os.system('git stash list')

    elif cmd == "gclean":
        os.system('git branch --merged | grep -v "\\*" | xargs git branch -d 2>/dev/null; echo "✅ 清理完成"')

    elif cmd == "gundo":
        os.system('git reset --soft HEAD~1 2>/dev/null || echo "❌ 无法撤销"')

    elif cmd == "gfork":
        os.system('git fetch origin && git rebase origin/$(git branch --show-current)')

    # ========== Docker 增强 ==========
    elif cmd == "dps":
        os.system('docker ps --format "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}"')

    elif cmd == "dpsa":
        os.system('docker ps -a --format "table {{.Names}}\\t{{.Status}}\\t{{.CreatedAt}}"')

    elif cmd == "dimages":
        os.system('docker images --format "table {{.Repository}}\\t{{.Tag}}\\t{{.Size}}"')

    elif cmd == "dstop":
        os.system('docker stop $(docker ps -q) 2>/dev/null; echo "✅ 所有容器已停止"')

    elif cmd == "drm":
        os.system('docker container prune -f; echo "✅ 清理完成"')

    elif cmd == "dlogs":
        if args:
            os.system('docker logs -f --tail 100 ' + args[0])
        else:
            print("用法: devtools dlogs <容器名>")

    elif cmd == "dexec":
        if len(args) >= 2:
            os.system('docker exec -it ' + args[0] + ' ' + ' '.join(args[1:]))
        else:
            print("用法: devtools dexec <容器名> <命令>")

    # ========== 系统工具 ==========
    elif cmd == "launchctl":
        if args:
            os.system('launchctl ' + ' '.join(args))
        else:
            os.system('launchctl list | head -30')

    elif cmd == "crontab":
        if args and args[0] == '-l':
            os.system('crontab -l')
        elif args and args[0] == '-e':
            os.system('crontab -e')
        else:
            print("用法: devtools crontab -l|-e")

    elif cmd == "lock":
        os.system('/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend')

    elif cmd == "restart":
        os.system('sudo shutdown -r now')

    elif cmd == "shutdown":
        os.system('sudo shutdown -h now')

    # ========== 进程增强 ==========
    elif cmd == "lsof":
        if args:
            os.system('lsof -i ' + args[0])
        else:
            os.system('lsof -i -P | head -30')

    elif cmd == "pgrep":
        if args:
            os.system('pgrep -l "' + args[0] + '"')
        else:
            print("用法: devtools pgrep <进程名>")

    elif cmd == "pkill":
        if args:
            os.system('pkill -f "' + ' '.join(args) + '"; echo "✅ 已终止"')
        else:
            print("用法: devtools pkill <进程名>")

    # ========== 网络增强 ==========
    elif cmd == "ssh":
        if args:
            os.system('ssh ' + ' '.join(args))
        else:
            print("用法: devtools ssh <用户@主机>")

    elif cmd == "scp":
        if len(args) >= 2:
            os.system('scp -r ' + args[0] + ' ' + args[1])
        else:
            print("用法: devtools scp <源> <目标>")

    elif cmd == "rsync":
        if len(args) >= 2:
            os.system('rsync -avz ' + args[0] + ' ' + args[1])
        else:
            print("用法: devtools rsync <源> <目标>")

    elif cmd == "wget":
        if args:
            os.system('wget -O ~/Downloads/$(basename ' + args[0] + ') ' + args[0])
        else:
            print("用法: devtools wget <URL>")

    elif cmd == "curl-post":
        if args:
            os.system('curl -X POST ' + ' '.join(args))
        else:
            print("用法: devtools curl-post <URL>")

    elif cmd == "curl-headers":
        if args:
            os.system('curl -I ' + args[0])
        else:
            print("用法: devtools curl-headers <URL>")

    # ========== 文件工具增强 ==========
    elif cmd == "extract":
        if args:
            import zipfile
            import tarfile
            f = args[0]
            if f.endswith('.zip'):
                zipfile.ZipFile(f).extractall('.')
            elif f.endswith('.tar.gz') or f.endswith('.tgz'):
                tarfile.open(f).extractall('.')
            elif f.endswith('.tar.bz2'):
                tarfile.open(f, 'r:bz2').extractall('.')
            print("✅ 已解压: " + f)
        else:
            print("用法: devtools extract <文件>")

    elif cmd == "backup":
        if args:
            src = args[0]
            dst = "~/Downloads/" + os.path.basename(src) + "_backup_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            os.system('cp -r ' + src + ' ' + dst)
            print("✅ 备份到: " + dst)
        else:
            print("用法: devtools backup <文件或目录>")

    # ========== 文本工具 ==========
    elif cmd == "jq":
        if args:
            os.system('echo "' + args[0] + '" | jq')
        else:
            print("用法: devtools jq <JSON>")

    elif cmd == "color":
        if args:
            try:
                r = int(args[0][0:2], 16)
                g = int(args[0][2:4], 16)
                b = int(args[0][4:6], 16)
                print("HEX: #" + args[0])
                print("RGB: (" + str(r) + ", " + str(g) + ", " + str(b) + ")")
            except:
                pass
        else:
            print("用法: devtools color <HEX>")

    # ========== macOS 特有功能 ==========
    elif cmd == "say":
        if args:
            os.system('say "' + ' '.join(args) + '"')
        else:
            print("用法: devtools say <文本>")

    elif cmd == "caffeinate":
        if args and args[0] == '-u':
            secs = int(args[1]) if len(args) > 1 else 3600
            os.system('caffeinate -u -t ' + str(secs))
        else:
            os.system('caffeinate -i &')

    elif cmd == "pmset":
        os.system('pmset -g everything | head -20')

    # ========== 开发增强 ==========
    elif cmd == "npm-outdated":
        os.system('npm outdated 2>/dev/null || echo "❌ 非 npm 项目"')

    elif cmd == "pip-list":
        os.system(sys.executable + ' -m pip list --outdated 2>/dev/null || pip3 list --outdated')

    elif cmd == "yarn":
        if args:
            os.system('yarn ' + ' '.join(args))
        else:
            os.system('yarn')

    elif cmd == "pnpm":
        if args:
            os.system('pnpm ' + ' '.join(args))
        else:
            os.system('pnpm')

    elif cmd == "bun":
        if args:
            os.system('bun ' + ' '.join(args))
        else:
            os.system('bun')

    elif cmd == "cargo":
        if args:
            os.system('cargo ' + ' '.join(args))
        else:
            os.system('cargo')

    # ========== 其他实用工具 ==========
    elif cmd == "weather":
        try:
            ip = urllib.request.urlopen('https://api.ipify.org', timeout=5).read().decode()
            data = urllib.request.urlopen('https://wttr.in/' + ip + '?format=j1', timeout=5).read().decode()
            info = json.loads(data)
            current = info['current_condition'][0]
            print("🌤️  当前: " + current['weatherDesc'][0]['value'])
            print("🌡️  温度: " + current['temp_C'] + "°C")
            print("💧 湿度: " + current['humidity'] + "%")
            print("💨 风速: " + current['windspeedKmph'] + " km/h")
        except Exception as e:
            print("❌ 获取天气失败: " + str(e))

    elif cmd == "qrdecode":
        if args:
            os.system('qrencode -t UTF8 "' + args[0] + '"')
        else:
            print("用法: devtools qrdecode <文本>")

    elif cmd == "hash":
        if args:
            text = ' '.join(args)
            print("MD5:    " + hashlib.md5(text.encode()).hexdigest())
            print("SHA1:   " + hashlib.sha1(text.encode()).hexdigest())
            print("SHA256: " + hashlib.sha256(text.encode()).hexdigest())
        else:
            print("用法: devtools hash <文本>")

    elif cmd == "alias":
        os.system('alias | head -30')

    elif cmd == "whatis":
        if args:
            os.system('whatis ' + args[0] + ' 2>/dev/null || man -w ' + args[0])

    elif cmd == "neofetch":
        import psutil
        print("""
        .:'                    """ + platform.node() + """
    .'' .;:                  -----------
    ,;. ::;'                   OS: """ + platform.system() + """ """ + platform.release() + """
   ;:;. '';'                  Host: """ + (platform.mac_ver()[0] or 'Unknown') + """
   '.;.:;.'`.;                Shell: """ + os.environ.get('SHELL', 'Unknown') + """
    '.;.::.::.              CPU: """ + (platform.processor() or 'Apple Silicon') + """
        '::'                 Memory: """ + str(round(psutil.virtual_memory().total/1024**3, 1)) + """ GB
""")

    elif cmd == "fortune":
        os.system('fortune 2>/dev/null || echo "安装 fortune: brew install fortune"')

    elif cmd == "sl":
        print("🚂 Choo Choo! Type ls instead!")

    elif cmd == "hack":
        print("""
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        """)

    elif cmd == "meow":
        print("""
    /\\_____/\\
   /  o   o  \\
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
""")

    elif cmd == "banana":
        print("🍌 Banana!")

    elif cmd == "rocket":
        print("       |       / \\      🚀")

    elif cmd == "spin":
        chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for _ in range(30):
            for c in chars:
                print('\r' + c + ' Loading... ', end='', flush=True)
                time.sleep(0.1)
        print('\r✅ 完成!')

    elif cmd == "countdown":
        if args:
            for i in range(int(args[0]), 0, -1):
                print('\r⏰ ' + str(i) + ' ', end='', flush=True)
                time.sleep(1)
            print('\r🔔 时间到!')
            if args[1:]:
                os.system('say "' + ' '.join(args[1:]) + '"')
        else:
            print("用法: devtools countdown <秒数> [提示语]")

    elif cmd == "pomodoro":
        print("🍅 Pomodoro Timer: 25分钟专注工作")
        for i in range(25, 0, -1):
            print('\r🍅 ' + str(i).zfill(2) + ':00 ', end='', flush=True)
            time.sleep(60)
        print('\r🔔 时间到! 休息5分钟')
        os.system('say "Pomodoro finished! Take a break."')

    elif cmd == "ipinfo":
        if args:
            ip = args[0]
        else:
            try:
                ip = urllib.request.urlopen('https://api.ipify.org', timeout=5).read().decode()
            except:
                ip = socket.gethostbyname(socket.gethostname())
        try:
            data = urllib.request.urlopen('https://ipapi.co/' + ip + '/json/', timeout=5).read().decode()
            info = json.loads(data)
            print("🌐 IP: " + ip)
            print("🏠 城市: " + (info.get('city') or 'N/A'))
            print("🌍 国家: " + (info.get('country_name') or 'N/A'))
            print("📍 地区: " + (info.get('region') or 'N/A'))
            print("🏢 ISP: " + (info.get('org') or 'N/A'))
        except Exception as e:
            print("❌ 查询失败: " + str(e))

    elif cmd == "shorten":
        if args:
            url = args[0]
            try:
                data = urllib.request.urlopen('https://tinyurl.com/api-create.php?url=' + url, timeout=5).read().decode()
                print("🔗 短链接: " + data)
            except Exception as e:
                print("❌ 缩短失败: " + str(e))
        else:
            print("用法: devtools shorten <URL>")

    elif cmd == "qr":
        if args:
            os.system('qrencode -t ANSIUTF8 "' + args[0] + '"')
        else:
            print("用法: devtools qr <文本或URL>")

    elif cmd == "clipboard":
        content = subprocess.run(['pbpaste'], capture_output=True, text=True).stdout
        print("📋 剪贴板内容 (" + str(len(content)) + " 字符):")
        print(content[:500] if len(content) > 500 else content)

    elif cmd == "clearlogs":
        os.system('sudo rm -rf /var/log/*.log 2>/dev/null; echo "✅ 日志清理完成"')

    elif cmd == "gcc":
        if args:
            src = args[0]
            out = args[1] if len(args) > 1 else 'a.out'
            os.system('gcc ' + src + ' -o ' + out)
        else:
            print("用法: devtools gcc <源文件> [输出文件]")

    elif cmd == "make":
        if args:
            os.system('make ' + args[0])
        else:
            os.system('make')

    elif cmd == "cmake":
        if args:
            os.system('cmake ' + args[0])
        else:
            print("用法: devtools cmake <目录>")


    # ========== 进程监控增强 ==========
    elif cmd == "process-tree":
        import psutil
        print("🌳 进程树 (前30个):")
        for proc in sorted(psutil.process_iter(['pid', 'name', 'ppid']), key=lambda x: x.info['ppid'] or 0)[:30]:
            try:
                pinfo = proc.info
                print(f"  {pinfo['pid']:>6} {pinfo['name'][:30]:<30} (PPID:{pinfo['ppid'] or 0})")
            except:
                pass

    elif cmd == "threadcount":
        import psutil
        total = sum(p.num_threads() for p in psutil.process_iter())
        print(f"🧵 总线程: {total}, 总进程: {len(list(psutil.process_iter()))}")

    elif cmd == "process-memory":
        if args:
            try:
                import psutil
                for p in psutil.process_iter(['pid', 'name']):
                    if args[0] in p.info['name']:
                        mem = p.memory_info()
                        print(f"{p.info['pid']:>6} {p.info['name'][:30]:<30} {mem.rss//1024//1024:>6}MB")
            except:
                print("用法: process-memory <名称>")
        else:
            print("用法: process-memory <名称>")

    elif cmd == "top-cpu":
        import psutil
        procs = []
        for p in psutil.process_iter():
            try:
                cpu = p.cpu_percent()
                procs.append((p, cpu))
            except:
                pass
        for p, cpu in sorted(procs, key=lambda x: x[1], reverse=True)[:10]:
            try:
                print(f"  {cpu:>5.1f}% {p.info['name'][:30]}")
            except:
                pass

    elif cmd == "top-mem":
        import psutil
        procs = []
        for p in psutil.process_iter():
            try:
                mem = p.memory_percent()
                procs.append((p, mem))
            except:
                pass
        for p, mem in sorted(procs, key=lambda x: x[1], reverse=True)[:10]:
            try:
                print(f"  {mem:>5.1f}% {p.info['name'][:30]}")
            except:
                pass

    # ========== 系统工具 ==========
    elif cmd == "sysreport":
        print("📋 系统报告")
        import psutil
        print(f"系统: {platform.system()} {platform.release()}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"CPU: {psutil.cpu_count(logical=False)}核 {psutil.cpu_percent()}%")
        print(f"内存: {psutil.virtual_memory().percent}%")
        print(f"磁盘: {psutil.disk_usage('/').percent}%")
        os.system('git --version 2>/dev/null | head -1')
        os.system('node --version 2>/dev/null')
        os.system('docker --version 2>/dev/null | head -1')

    elif cmd == "syshealth":
        import psutil
        checks = [
            ("CPU", psutil.cpu_percent() < 80),
            ("内存", psutil.virtual_memory().percent < 80),
            ("磁盘", psutil.disk_usage('/').percent < 90),
        ]
        print("🏥 系统健康检查:")
        for name, ok in checks:
            print(f"  {'✅' if ok else '❌'} {name}")

    elif cmd == "memory-graph":
        import psutil
        vm = psutil.virtual_memory()
        used = int(vm.percent / 2)
        print(f"💾 [{'█'*used}{'░'*(50-used)}] {vm.percent}%")

    elif cmd == "cpu-graph":
        import psutil
        cpu = int(psutil.cpu_percent())
        print(f"🔥 [{'█'*int(cpu/2)}{'░'*(50-int(cpu/2))}] {cpu}%")

    elif cmd == "model":
        os.system("sysctl -n hw.model 2>/dev/null")

    elif cmd == "boot":
        result = subprocess.run(['sysctl', '-n', 'kern.boottime'], capture_output=True, text=True)
        print(result.stdout.strip())

    elif cmd == "uprecords":
        os.system('uptime | sed "s/.*up/up/"')

    elif cmd == "users":
        os.system('who 2>/dev/null || echo "无其他用户"')

    elif cmd == "disk-info":
        import psutil
        for p in psutil.disk_partitions():
            try:
                u = psutil.disk_usage(p.mountpoint)
                print(f"{p.device} ({p.mountpoint}): {u.total//1024**3}GB, {u.percent}% used")
            except:
                pass

    elif cmd == "disk-check":
        import psutil
        d = psutil.disk_usage('/')
        print(f"总计: {d.total//1024**3}GB")
        print(f"已用: {d.used//1024**3}GB ({d.percent}%)")
        print(f"可用: {d.free//1024**3}GB")

    elif cmd == "memory-check":
        import psutil
        m = psutil.virtual_memory()
        print(f"总计: {m.total//1024**3:.1f}GB")
        print(f"已用: {m.used//1024**3:.1f}GB ({m.percent}%)")
        print(f"可用: {m.available//1024**3:.1f}GB")

    elif cmd == "cpu-arch":
        print(f"架构: {platform.machine()}")
        print(f"64位: {platform.machine() in ['x86_64', 'arm64']}")

    elif cmd == "cpuinfo":
        import psutil
        cpu_freq = psutil.cpu_freq()
        print(f"🔥 CPU: {psutil.cpu_count(logical=False)} 核 / {psutil.cpu_count(logical=True)} 线程")
        if cpu_freq:
            print(f"📊 频率: {cpu_freq.current:.0f} MHz")

    # ========== 网络增强 ==========
    elif cmd == "publicip-detail":
        import json
        try:
            data = json.loads(urllib.request.urlopen('https://ipinfo.io/json', timeout=5).read())
            print(f"IP: {data.get('ip')}")
            print(f"城市: {data.get('city')}")
            print(f"地区: {data.get('region')}")
            print(f"国家: {data.get('country')}")
            print(f"组织: {data.get('org')}")
        except Exception as e:
            print(f"用法: publicip-detail")

    elif cmd == "publicip":
        try:
            print(urllib.request.urlopen('https://ipinfo.io/ip', timeout=3).read().decode().strip())
        except:
            pass

    elif cmd == "ports-known":
        print("📡 常用端口:")
        ports = {"21":"FTP","22":"SSH","25":"SMTP","53":"DNS","80":"HTTP","443":"HTTPS","3306":"MySQL","5432":"PostgreSQL","6379":"Redis","8080":"HTTP-Alt","27017":"MongoDB"}
        for p,t in ports.items():
            print(f"  {p}: {t}")

    elif cmd == "ports-listen":
        print("📡 监听端口:")
        os.system('lsof -i -P | grep LISTEN 2>/dev/null')

    elif cmd == "connections-all":
        print("🌐 ESTABLISHED 连接:")
        os.system('netstat -an | grep ESTABLISHED | wc -l')

    elif cmd == "dnslookup":
        if args:
            try:
                ip = socket.gethostbyname(args[0])
                print(f"{args[0]} -> {ip}")
            except:
                print(f"无法解析: {args[0]}")
        else:
            print("用法: dnslookup <域名>")

    elif cmd == "reverse-dns":
        if args:
            try:
                name = socket.gethostbyaddr(args[0])
                print(f"{args[0]} -> {name[0]}")
            except:
                print(f"无法反向解析: {args[0]}")
        else:
            print("用法: reverse-dns <IP>")

    elif cmd == "httptest":
        if args:
            url = args[0]
            os.system(f'curl -s -o /dev/null -w "状态码: %{{http_code}}\n耗时: %{{time_total}}s\n大小: %{{size_download}}B\n" "{url}"')
        else:
            print("用法: httptest <url>")

    # ========== Git 增强 ==========
    elif cmd == "glogf":
        os.system("git log --oneline --graph --all --decorate -20 2>/dev/null")

    elif cmd == "gcontributors":
        os.system("git shortlog -sn 2>/dev/null | head -20 || echo '非 Git 目录'")

    elif cmd == "glast":
        os.system("git log -1 --format='%H%n%an%n%ae%n%ar%n%s' 2>/dev/null || echo '非 Git 目录'")

    # ========== Docker 增强 ==========
    elif cmd == "docker-clean":
        print("🧹 Docker 清理")
        os.system('docker system prune -f 2>/dev/null || echo "需要 Docker"')

    elif cmd == "docker-stats":
        os.system('docker stats --no-stream 2>/dev/null || echo "需要 Docker"')

    # ========== 文件工具 ==========
    elif cmd == "find-duplicates":
        print("🔍 查找重复文件")
        os.system('find ~/Documents -type f 2>/dev/null | head -50 | xargs -I{} md5 {} 2>/dev/null | sort | uniq -D | head -10')

    elif cmd == "clean-temp":
        print("🧹 清理临时文件")
        os.system('rm -rf /tmp/*.log /tmp/*.tmp 2>/dev/null')
        print("✅ 清理完成")

    elif cmd == "disk-usage-tree":
        print("📊 目录大小树")
        if args:
            os.system(f'du -sh "{args[0]}"/* 2>/dev/null | sort -rh | head -20')
        else:
            os.system('du -sh ~/Documents/* ~/Downloads/* 2>/dev/null | sort -rh | head -20')

    elif cmd == "file-type-count":
        print("📁 文件类型统计")
        os.system('find ~/Documents -type f 2>/dev/null | sed "s/.*\.//" | sort | uniq -c | sort -rn | head -20')

    elif cmd == " newest":
        days = int(args[0]) if args and args[0].isdigit() else 7
        print(f"📂 最近 {days} 天修改的文件:")
        os.system(f'find ~ -type f -mtime -{days} 2>/dev/null | head -30')

    elif cmd == "md5file":
        if args:
            import hashlib
            h = hashlib.md5()
            with open(args[0], 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
            print(f"MD5: {h.hexdigest()}")
        else:
            print("用法: md5file <文件>")

    elif cmd == "sha256file":
        if args:
            import hashlib
            h = hashlib.sha256()
            with open(args[0], 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
            print(f"SHA256: {h.hexdigest()}")
        else:
            print("用法: sha256file <文件>")

    elif cmd == "sha1file":
        if args:
            import hashlib
            h = hashlib.sha1()
            with open(args[0], 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
            print(f"SHA1: {h.hexdigest()}")
        else:
            print("用法: sha1file <文件>")

    elif cmd == "file-info":
        if args:
            try:
                s = os.stat(args[0])
                print(f"文件: {args[0]}")
                print(f"大小: {s.st_size} bytes")
                print(f"权限: {oct(s.st_mode)[-3:]}")
                print(f"修改: {datetime.datetime.fromtimestamp(s.st_mtime)}")
            except:
                print("用法: file-info <文件>")
        else:
            print("用法: file-info <文件>")

    # ========== 文本处理 ==========
    elif cmd == "head":
        n = 10
        if args and args[0].isdigit():
            n = int(args.pop(0))
        if args:
            print(''.join(open(args[0]).readlines()[:n]))
        else:
            
            print(''.join(_sys_stdin.stdin.readlines()[:n]))

    elif cmd == "tail":
        n = 10
        if args and args[0].isdigit():
            n = int(args.pop(0))
        if args:
            lines = open(args[0]).readlines()
            print(''.join(lines[-n:]))
        else:
            
            lines = _sys_stdin.stdin.readlines()
            print(''.join(lines[-n:]))

    # ========== 编码工具 ==========
    elif cmd == "hex":
        if args:
            print(' '.join(args).encode().hex())
        else:
            print("用法: hex <文本>")

    elif cmd == "unhex":
        if args:
            print(bytes.fromhex(' '.join(args)).decode())
        else:
            print("用法: unhex <十六进制>")

    elif cmd == "rot13":
        if args:
            text = ' '.join(args)
            print(text.encode('rot13').decode('rot13'))
        else:
            print("用法: rot13 <文本>")

    elif cmd == "base32":
        if args:
            import base64
            print(base64.b32encode(' '.join(args).encode()).decode())
        else:
            print("用法: base32 <文本>")

    elif cmd == "binary":
        if args:
            print(' '.join(format(ord(c),'08b') for c in ' '.join(args)))
        else:
            print("用法: binary <文本>")

    # ========== 时间工具 ==========
    elif cmd == "timestamp":
        print(int(datetime.datetime.now().timestamp()))

    elif cmd == "epoch":
        if args:
            try:
                ts = int(args[0])
                print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
            except:
                print("用法: epoch <时间戳>")

    elif cmd == "week":
        today = datetime.datetime.now()
        print(f"Week {today.isocalendar()[1]}, {today.strftime('%A')}")

    elif cmd == "month":
        import calendar
        print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))

    elif cmd == "datediff":
        if len(args) >= 2:
            try:
                d1 = datetime.datetime.strptime(args[0], '%Y-%m-%d')
                d2 = datetime.datetime.strptime(args[1], '%Y-%m-%d')
                print(f"相差: {(d2-d1).days} 天")
            except:
                print("用法: datediff 2026-01-01 2026-12-31")

    elif cmd == "date-add":
        if len(args) >= 2:
            try:
                delta = datetime.timedelta(days=int(args[0]))
                print((datetime.datetime.now() + delta).strftime("%Y-%m-%d"))
            except:
                print("用法: date-add 7 days")
        else:
            print("用法: date-add 7 days")

    # ========== 数学工具 ==========
    elif cmd == "prime":
        if args:
            n = int(args[0])
            p = [i for i in range(2,n+1) if all(i%j for j in range(2,int(i**0.5)+1))]
            print(f"1-{n}: {len(p)} primes")
        else:
            print("用法: prime <数字>")

    elif cmd == "fibonacci":
        if args:
            n = int(args[0])
            f = [0,1]
            for _ in range(n-2): f.append(f[-1]+f[-2])
            print(', '.join(map(str, f)))
        else:
            print("用法: fibonacci <数量>")

    elif cmd == "palindrome":
        if args:
            t = ' '.join(args)
            print(f"'{t}' is {'palindrome' if t==t[::-1] else 'not palindrome'}")
        else:
            print("用法: palindrome <文本>")

    elif cmd == "reverse":
        if args:
            print(' '.join(args)[::-1])
        else:
            print("用法: reverse <文本>")

    elif cmd == "length":
        if args:
            t = ' '.join(args)
            print(f"{len(t)} chars, {len(t.split())} words")
        else:
            print("用法: length <文本>")

    # ========== 密码工具 ==========
    elif cmd == "strongpass":
        l = int(args[0]) if args and args[0].isdigit() else 20
        p = ''.join(secrets.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(l))
        print(f"🔐 {p}")
        subprocess.run(['pbcopy'], input=p.encode())

    elif cmd == "pin":
        l = int(args[0]) if args and args[0].isdigit() else 6
        print(f"🔢 {''.join(secrets.choice(string.digits) for _ in range(l))}")

    elif cmd == "uuid":
        print(f"🔑 {uuid.uuid4()}")

    # ========== 包管理 ==========
    elif cmd == "upgrades":
        print("🔄 可更新的包:")
        os.system('pip list -o 2>/dev/null | head -20')

    elif cmd == "brew-outdated":
        os.system('brew outdated 2>/dev/null | head -20 || echo "需要 Homebrew"')

    # ========== Cron 工具 ==========
    elif cmd == "cronlist":
        os.system('crontab -l 2>/dev/null || echo "无定时任务"')

    elif cmd == "services":
        os.system('launchctl list 2>/dev/null | head -30')

    # ========== 系统管理 ==========
    elif cmd == "killall":
        if args:
            os.system(f'pkill -f "{args[0]}" && echo "已终止 {args[0]}"')
        else:
            print("用法: killall <进程名>")

    elif cmd == "boot":
        import subprocess
        result = subprocess.run(['sysctl', '-n', 'kern.boottime'], capture_output=True, text=True)
        print(result.stdout.strip())

    elif cmd == "envcheck":
        print(f"Python: {sys.version.split()[0]}")
        os.system('node --version 2>/dev/null')
        os.system('git --version 2>/dev/null')

    elif cmd == "platform":
        print(f"系统: {platform.system()}")
        print(f"版本: {platform.version()}")

    elif cmd == "syspath":
        print("\n".join(sys.path))

    elif cmd == "tz":
        print(f"时区: Asia/Shanghai (GMT+8)")

    # ========== 加密工具 ==========
    elif cmd == "jwt-decode":
        if args:
            try:
                parts = args[0].split('.')
                if len(parts) == 3:
                    payload = json.loads(base64.b64decode(parts[1]+'==').decode())
                    print(json.dumps(payload, indent=2))
            except:
                print("用法: jwt-decode <JWT>")
        else:
            print("用法: jwt-decode <JWT>")

    elif cmd == "hmac":
        if len(args) >= 2:
            import hmac as _hmac, hashlib
            print(_hmac.new(args[0].encode(), args[1].encode(), hashlib.sha256).hexdigest())
        else:
            print("用法: hmac <key> <message>")

    elif cmd == "ssl":
        if args:
            os.system(f'echo | openssl s_client -connect {args[0]} 2>/dev/null | head -10 || echo "用法: ssl <域名>"')
        else:
            print("用法: ssl <域名>")

    # ========== Todo 列表 ==========
    elif cmd == "todo":
        print("📝 Todo List")
        try:
            todos = open('/tmp/devtools_todo.txt').read().strip()
            for i, t in enumerate(todos.splitlines(), 1):
                print(f"  {i}. {t}")
        except:
            print("暂无待办 | 用法: devtools addtodo <事项>")

    elif cmd == "addtodo":
        if args:
            with open('/tmp/devtools_todo.txt', 'a') as f:
                f.write(' '.join(args) + '\n')
            print("✅ 已添加: " + ' '.join(args))

    elif cmd == "done":
        if args:
            try:
                todos = open('/tmp/devtools_todo.txt').read().strip().splitlines()
                idx = int(args[0]) - 1
                if 0 <= idx < len(todos):
                    done = todos.pop(idx)
                    open('/tmp/devtools_todo.txt', 'w').write('\n'.join(todos))
                    print("✅ 完成: " + done)
            except:
                print("用法: done <序号>")

    # ========== 杂项 ==========
    elif cmd == "ports":
        print("📡 端口扫描 (常用端口):")
        for p in [21,22,25,53,80,443,3306,5432,6379,8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex(('localhost', p))
            if result == 0:
                print(f"  {p}: OPEN")
            sock.close()

    elif cmd == "ascii-table":
        for i in range(33,127,16):
            print(' '.join(chr(j) for j in range(i,min(i+16,127))))

    elif cmd == "emoji":
        print("🚀 💡 🔥 ⭐ ✨ 🎯 💪 🛠️ 📦 🖥️ 🌐 📝 ✅ ❌ ⚠️")

    elif cmd == "colors":
        for i in range(16):
            print(f"\033[4{i}m {i:2} \033[0m", end=' ')
        print()

    elif cmd == "anagram":
        if args:
            import itertools
            w = args[0].upper()
            print(', '.join(set(''.join(p) for p in itertools.permutations(w)))[:100])
        else:
            print("用法: anagram <单词>")

    elif cmd == "palindromes":
        print(', '.join(["level","radar","civic","refer","rotor"]))

    elif cmd == "spell":
        if args:
            w = ' '.join(args)
            print(f"✏️ {w} ({len(w)} letters)")
        else:
            print("用法: spell <单词>")

    elif cmd == "whois":
        if args:
            os.system(f'whois {args[0]} 2>/dev/null | head -15 || echo "用法: whois <域名>"')
        else:
            print("用法: whois <域名>")

    elif cmd == "dns-records":
        if args:
            for t in ['A', 'MX', 'NS']:
                os.system(f'dig +short {args[0]} {t} 2>/dev/null | head -1')
        else:
            print("用法: dns-records <域名>")

    elif cmd == "subnet":
        if len(args) >= 2:
            import ipaddress
            try:
                n = ipaddress.ip_network(args[0]+'/'+args[1], strict=False)
                print(f"网络: {n.network_address}, 主机: {n.num_addresses-2}")
            except:
                print("用法: subnet <IP> <CIDR>")
        else:
            print("用法: subnet <IP> <CIDR>")

    else:
        print("❌ 未知命令: " + cmd)
        print("💡 输入 'devtools' 查看所有命令")

if __name__ == "__main__":
    main()
