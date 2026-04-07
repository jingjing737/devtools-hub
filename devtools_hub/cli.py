#!/usr/bin/env python3
"""DevTools Hub CLI"""
import sys
import subprocess
import json
import time

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
🔧 DevTools Hub - 开发者工具集

用法: devtools <命令>

命令:
  start    启动服务
  stop     停止服务
  status   系统状态
  cpu      CPU 信息
  mem      内存信息
  disk     磁盘信息
  net      网络速度
  top      高占用进程
  bench    性能测试
""")
        return

    cmd = sys.argv[1]

    if cmd == "start":
        print("🚀 启动服务...")
        subprocess.Popen([sys.executable, "-m", "devtools_hub.server"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)
        print(f"✅ 已启动: {URL}")

    elif cmd == "stop":
        subprocess.run(["pkill", "-f", "devtools_hub.server"])
        print("✅ 已停止")

    elif cmd == "status":
        if check():
            import requests
            r = requests.get(f"{URL}/api/health")
            print(json.dumps(r.json(), indent=2))
        else:
            print("❌ 服务未运行，请先 devtools start")

    elif cmd == "cpu":
        if check():
            import requests
            r = requests.get(f"{URL}/api/system")
            d = r.json()
            print(f"CPU: {d.get('cpu_percent', '?')}%")
        else:
            print("❌ 服务未运行")

    elif cmd == "mem":
        if check():
            import requests
            r = requests.get(f"{URL}/api/system")
            d = r.json()
            print(f"内存: {d.get('memory_percent', '?')}%")
        else:
            print("❌ 服务未运行")

    elif cmd == "top":
        if check():
            import requests
            r = requests.get(f"{URL}/api/processes/top")
            d = r.json()
            print("🔥 CPU:")
            for p in d.get("by_cpu", [])[:5]:
                print(f"  {p['name']}: {p['cpu']}%")
            print("💾 内存:")
            for p in d.get("by_memory", [])[:5]:
                print(f"  {p['name']}: {p['memory']}%")
        else:
            print("❌ 服务未运行")

    elif cmd == "net":
        if check():
            import requests
            r = requests.get(f"{URL}/api/network/bandwidth")
            d = r.json()
            print(f"↑{d.get('upload_mbps', 0)} Mbps  ↓{d.get('download_mbps', 0)} Mbps")
        else:
            print("❌ 服务未运行")

    elif cmd == "bench":
        if check():
            import requests
            r = requests.get(f"{URL}/api/benchmark/full")
            print(json.dumps(r.json(), indent=2))
        else:
            print("❌ 服务未运行")

    else:
        print(f"❌ 未知命令: {cmd}")

if __name__ == "__main__":
    main()
