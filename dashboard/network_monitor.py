"""Network Monitoring API"""
from flask import Blueprint, jsonify
import psutil
import socket
import time

network_bp = Blueprint('network', __name__)

# Track bandwidth over time
bandwidth_history = []
MAX_HISTORY = 60

last_net_io = psutil.net_io_counters()
last_time = time.time()

def get_bandwidth():
    """Calculate current bandwidth"""
    global last_net_io, last_time
    current = psutil.net_io_counters()
    now = time.time()
    elapsed = now - last_time
    
    if elapsed > 0:
        upload_speed = (current.bytes_sent - last_net_io.bytes_sent) / elapsed
        download_speed = (current.bytes_recv - last_net_io.bytes_recv) / elapsed
    else:
        upload_speed, download_speed = 0, 0
    
    last_net_io = current
    last_time = now
    
    return {
        'upload_bps': int(upload_speed),
        'download_bps': int(download_speed),
        'upload_mbps': round(upload_speed * 8 / 1_000_000, 2),
        'download_mbps': round(download_speed * 8 / 1_000_000, 2)
    }

@network_bp.route('/api/network/bandwidth')
def bandwidth():
    """Get current bandwidth"""
    return jsonify(get_bandwidth())

@network_bp.route('/api/network/interfaces')
def interfaces():
    """Get network interfaces"""
    result = []
    for name, addrs in psutil.net_if_addrs().items():
        iface = {'name': name, 'addresses': []}
        for addr in addrs:
            iface['addresses'].append({
                'family': socket.AddressFamily(addr.family).name,
                'address': addr.address,
                'netmask': addr.netmask,
                'broadcast': addr.broadcast
            })
        result.append(iface)
    return jsonify({'interfaces': result})

@network_bp.route('/api/network/connections')
def connections():
    """Get network connections"""
    conns = []
    for c in psutil.net_connections(kind='inet'):
        conns.append({
            'fd': c.fd,
            'family': socket.AddressFamily(c.family).name,
            'type': socket.SocketKind(c.type).name,
            'local_addr': f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else None,
            'remote_addr': f"{c.raddr.ip}:{c.raddr.port}" if c.raddr else None,
            'status': c.status,
            'pid': c.pid
        })
    return jsonify({'connections': conns, 'count': len(conns)})

@network_bp.route('/api/network/stats')
def stats():
    """Get network statistics"""
    io = psutil.net_io_counters()
    return jsonify({
        'bytes_sent': io.bytes_sent,
        'bytes_recv': io.bytes_recv,
        'packets_sent': io.packets_sent,
        'packets_recv': io.packets_recv,
        'errin': io.errin,
        'errout': io.errout,
        'dropin': io.dropin,
        'dropout': io.dropout
    })
