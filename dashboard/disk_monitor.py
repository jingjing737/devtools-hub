"""Disk Monitoring API"""
from flask import Blueprint, jsonify
import psutil
import shutil
import os

disk_bp = Blueprint('disk', __name__)

@disk_bp.route('/api/disk/usage')
def disk_usage():
    """Get disk usage for all partitions"""
    partitions = []
    for p in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(p.mountpoint)
            partitions.append({
                'device': p.device,
                'mountpoint': p.mountpoint,
                'fstype': p.fstype,
                'total_gb': round(usage.total / (1024**3), 1),
                'used_gb': round(usage.used / (1024**3), 1),
                'free_gb': round(usage.free / (1024**3), 1),
                'percent': usage.percent
            })
        except PermissionError:
            pass
    return jsonify({'partitions': partitions})

@disk_bp.route('/api/disk/io')
def disk_io():
    """Get disk I/O statistics"""
    io = psutil.disk_io_counters()
    return jsonify({
        'read_count': io.read_count,
        'write_count': io.write_count,
        'read_bytes': io.read_bytes,
        'write_bytes': io.write_bytes,
        'read_mb': round(io.read_bytes / (1024**2), 1),
        'write_mb': round(io.write_bytes / (1024**2), 1)
    })

@disk_bp.route('/api/disk/largest-files')
def largest_files():
    """Find largest files in home directory"""
    home = os.path.expanduser('~')
    files = []
    for root, dirs, filenames in os.walk(home):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in filenames:
            try:
                path = os.path.join(root, f)
                size = os.path.getsize(path)
                if size > 100 * 1024 * 1024:  # > 100MB
                    files.append({
                        'path': path,
                        'size_mb': round(size / (1024**2), 1)
                    })
            except:
                pass
            if len(files) >= 20:
                break
        if len(files) >= 20:
            break
    files.sort(key=lambda x: x['size_mb'], reverse=True)
    return jsonify({'files': files[:10]})

@disk_bp.route('/api/disk/temp')
def temp_files():
    """Get temp directory size"""
    temp_dirs = ['/tmp', '/var/tmp']
    result = []
    for d in temp_dirs:
        if os.path.exists(d):
            total = 0
            for root, dirs, files in os.walk(d):
                for f in files:
                    try:
                        total += os.path.getsize(os.path.join(root, f))
                    except:
                        pass
            result.append({'path': d, 'size_mb': round(total / (1024**2), 1)})
    return jsonify({'temp_dirs': result})
