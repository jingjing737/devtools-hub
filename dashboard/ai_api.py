#!/usr/bin/env python3
"""
DevTools Hub - AI Integration API
Provides AI-powered system management commands
"""
from flask import Flask, request, jsonify
import subprocess
import psutil
import os

app = Flask(__name__)

# AI Command Router
AI_COMMANDS = {
    "系统状态": "status",
    "进程列表": "processes",
    "磁盘使用": "disk",
    "内存使用": "memory",
    "CPU使用": "cpu",
    "网络连接": "network",
}

@app.route('/api/ai', methods=['POST'])
def ai_command():
    """Process natural language commands"""
    data = request.json
    command = data.get('command', '')
    
    # Route to appropriate handler
    if any(kw in command for kw in ['状态', 'status', '系统']):
        return jsonify(get_system_overview())
    
    elif any(kw in command for kw in ['进程', 'process', '程序']):
        return jsonify({"processes": get_top_processes()})
    
    elif any(kw in command for kw in ['内存', 'memory', 'RAM']):
        return jsonify(get_memory_info())
    
    elif any(kw in command for kw in ['磁盘', 'disk', '空间']):
        return jsonify(get_disk_info())
    
    elif any(kw in command for kw in ['网络', 'network', '连接']):
        return jsonify(get_network_info())
    
    elif any(kw in command for kw in ['CPU', 'cpu', '处理器']):
        return jsonify(get_cpu_info())
    
    else:
        return jsonify({
            "response": "我理解你的命令了",
            "available_commands": list(AI_COMMANDS.keys())
        })

def get_system_overview():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": psutil.boot_time()
    }

def get_top_processes():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procs.append(p.info)
        except:
            pass
    procs.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
    return procs[:10]

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total": f"{mem.total / (1024**3):.1f}GB",
        "used": f"{mem.used / (1024**3):.1f}GB",
        "free": f"{mem.available / (1024**3):.1f}GB",
        "percent": mem.percent
    }

def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "total": f"{disk.total / (1024**3):.1f}GB",
        "used": f"{disk.used / (1024**3):.1f}GB",
        "free": f"{disk.free / (1024**3):.1f}GB",
        "percent": disk.percent
    }

def get_network_info():
    net = psutil.net_io_counters()
    return {
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv,
        "packets_sent": net.packets_sent,
        "packets_recv": net.packets_recv
    }

def get_cpu_info():
    return {
        "percent": psutil.cpu_percent(interval=1),
        "count": psutil.cpu_count(),
        "freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
    }

if __name__ == '__main__':
    app.run(port=5002, debug=True)
