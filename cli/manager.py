#!/usr/bin/env python3
"""
DevTools Hub - System Manager CLI
Usage: python manager.py [command]
Commands:
    status      - Show system status
    processes   - List top processes
    kill <pid>  - Kill a process
    logs        - Show recent logs
    backup      - Backup important files
"""
import os
import sys
import psutil
import subprocess
from datetime import datetime

def get_system_status():
    """Get system status"""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu": f"{cpu}%",
        "memory": f"{memory.percent}%",
        "memory_used": f"{memory.used / (1024**3):.1f}GB / {memory.total / (1024**3):.1f}GB",
        "disk": f"{disk.percent}%",
        "disk_free": f"{disk.free / (1024**3):.1f}GB / {disk.total / (1024**3):.1f}GB",
        "uptime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }

def list_processes(sort_by='cpu', limit=10):
    """List top processes"""
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(p.info)
        except:
            pass
    
    # Sort and limit
    if sort_by == 'cpu':
        processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
    else:
        processes.sort(key=lambda x: x.get('memory_percent', 0), reverse=True)
    
    return processes[:limit]

def kill_process(pid):
    """Kill a process"""
    try:
        p = psutil.Process(pid)
        p.terminate()
        return f"Process {pid} terminated"
    except Exception as e:
        return f"Error: {e}"

def show_logs(lines=50):
    """Show system logs"""
    try:
        # Try journalctl on macOS
        result = subprocess.run(
            ["log", "show", "--predicate", "eventMessage contains 'error'", 
             "--last", "1h", "--limit", str(lines)],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout or "No recent errors"
    except:
        return "Log access not available"

def backup_files():
    """Backup important files"""
    backup_dir = os.path.expanduser("~/Desktop/backups")
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_dir}/backup_{timestamp}.tar.gz"
    
    # Backup config files
    configs = [
        os.path.expanduser("~/.zshrc"),
        os.path.expanduser("~/.gitconfig"),
    ]
    
    existing = [c for c in configs if os.path.exists(c)]
    if existing:
        result = subprocess.run(
            ["tar", "-czf", backup_file] + existing,
            capture_output=True
        )
        if result.returncode == 0:
            return f"Backup saved to: {backup_file}"
    
    return "No files to backup"

def main():
    if len(sys.argv) < 2:
        print("DevTools Hub CLI")
        print("Usage: python manager.py [status|processes|logs|backup]")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "status":
        status = get_system_status()
        print("=== System Status ===")
        for k, v in status.items():
            print(f"{k}: {v}")
    
    elif cmd == "processes":
        procs = list_processes()
        print("=== Top Processes (by CPU) ===")
        print(f"{'PID':<8} {'Name':<20} {'CPU%':<8} {'Memory%':<8}")
        for p in procs:
            print(f"{p['pid']:<8} {p['name'][:20]:<20} {p['cpu_percent']:<8} {p['memory_percent']:<8}")
    
    elif cmd == "logs":
        print(show_logs())
    
    elif cmd == "backup":
        print(backup_files())
    
    elif cmd == "kill" and len(sys.argv) > 2:
        print(kill_process(int(sys.argv[2])))
    
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
