"""Health Check API - System health monitoring and diagnostics"""
from flask import Blueprint, jsonify
import subprocess
import platform
import psutil
import time
import os

health_bp = Blueprint('health', __name__)

def get_disk_speed():
    """Measure disk read/write speed"""
    test_file = '/tmp/.devtools_speed_test'
    data = b'0' * (10 * 1024 * 1024)  # 10MB
    start = time.time()
    with open(test_file, 'wb') as f:
        f.write(data)
    write_speed = len(data) / (time.time() - start) / (1024*1024)
    start = time.time()
    with open(test_file, 'rb') as f:
        f.read()
    read_speed = len(data) / (time.time() - start) / (1024*1024)
    os.remove(test_file)
    return round(write_speed, 1), round(read_speed, 1)

def get_network_info():
    """Get network interfaces and stats"""
    addrs = psutil.net_if_addrs()
    io = psutil.net_io_counters()
    result = {}
    for iface, addr_list in addrs.items():
        ips = [a.address for a in addr_list if a.family == 2]
        if ips:
            result[iface] = ips
    return {
        "interfaces": result,
        "bytes_sent": io.bytes_sent,
        "bytes_recv": io.bytes_recv,
        "packets_sent": io.packets_sent,
        "packets_recv": io.packets_recv
    }

@health_bp.route('/api/health')
def health_check():
    """Full system health check"""
    load = os.getloadavg() if hasattr(os, 'getloadavg') else [0,0,0]
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    days = int(uptime // 86400)
    hours = int((uptime % 86400) // 3600)
    
    try:
        w_speed, r_speed = get_disk_speed()
    except:
        w_speed, r_speed = 0, 0
    
    return jsonify({
        "status": "healthy",
        "system": {
            "platform": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "hostname": platform.node(),
            "processor": platform.processor(),
            "uptime": f"{days}d {hours}h",
            "load_avg": [round(l, 2) for l in load],
            "cpu_cores_physical": psutil.cpu_count(logical=False),
            "cpu_cores_logical": psutil.cpu_count(logical=True)
        },
        "memory": {
            "total_gb": round(psutil.virtual_memory().total / (1024**3), 1),
            "available_gb": round(psutil.virtual_memory().available / (1024**3), 1),
            "percent": psutil.virtual_memory().percent
        },
        "disk": {
            "write_speed_mbps": w_speed,
            "read_speed_mbps": r_speed
        },
        "network": get_network_info()
    })

@health_bp.route('/api/health/cpu-history')
def cpu_history():
    """Get CPU usage samples"""
    samples = []
    for _ in range(10):
        samples.append(psutil.cpu_percent(interval=0.1))
    return jsonify({
        "samples": samples,
        "avg": round(sum(samples) / len(samples), 1),
        "max": max(samples),
        "min": min(samples)
    })

@health_bp.route('/api/health/services')
def check_services():
    """Check common service status"""
    services = []
    ports = {
        "HTTP (80)": 80,
        "HTTPS (443)": 443,
        "SSH (22)": 22,
        "MySQL (3306)": 3306,
        "PostgreSQL (5432)": 5432,
        "Redis (6379)": 6379,
        "MongoDB (27017)": 27017,
        "Docker (2375)": 2375,
        "Ollama (11434)": 11434,
        "DevTools (5001)": 5001
    }
    for name, port in ports.items():
        try:
            s = __import__('socket').socket()
            s.settimeout(0.5)
            result = s.connect_ex(('127.0.0.1', port))
            s.close()
            services.append({"name": name, "port": port, "status": "running" if result == 0 else "stopped"})
        except:
            services.append({"name": name, "port": port, "status": "unknown"})
    return jsonify({"services": services})

@health_bp.route('/api/health/battery')
def battery_info():
    """Get battery status"""
    battery = psutil.sensors_battery()
    if battery:
        return jsonify({
            "percent": battery.percent,
            "plugged": battery.power_plugged,
            "remaining": f"{battery.secsleft // 60}m" if battery.secsleft >= 0 else "N/A"
        })
    return jsonify({"status": "not_available"})
