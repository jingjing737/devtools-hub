"""Advanced Process Monitor with AI Insights"""
from flask import Blueprint, jsonify, request
import psutil
import time
from collections import defaultdict

monitor_bp = Blueprint('monitor', __name__)

# Process history for trending
process_history = defaultdict(list)
MAX_HISTORY = 100

def get_process_tree():
    """Get process tree with parent-child relationships"""
    procs = []
    for p in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time']):
        try:
            info = p.info
            procs.append({
                'pid': info['pid'],
                'ppid': info['ppid'],
                'name': info['name'],
                'cpu': round(info['cpu_percent'] or 0, 1),
                'memory': round(info['memory_percent'] or 0, 1),
                'status': info['status'],
                'uptime': int(time.time() - info['create_time'])
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return procs

def find_top_processes(procs, by='cpu', n=10):
    """Find top N processes by metric"""
    return sorted(procs, key=lambda x: x[by], reverse=True)[:n]

def detect_anomalies(procs):
    """Detect unusual process behavior"""
    anomalies = []
    for p in procs:
        if p['cpu'] > 80:
            anomalies.append({'pid': p['pid'], 'name': p['name'], 'type': 'high_cpu', 'value': p['cpu']})
        if p['memory'] > 50:
            anomalies.append({'pid': p['pid'], 'name': p['name'], 'type': 'high_memory', 'value': p['memory']})
    return anomalies

@monitor_bp.route('/api/processes/tree')
def process_tree():
    """Get full process tree"""
    return jsonify({'processes': get_process_tree(), 'count': len(get_process_tree())})

@monitor_bp.route('/api/processes/top')
def top_processes():
    """Get top processes by CPU and memory"""
    procs = get_process_tree()
    return jsonify({
        'by_cpu': find_top_processes(procs, 'cpu'),
        'by_memory': find_top_processes(procs, 'memory'),
        'total': len(procs)
    })

@monitor_bp.route('/api/processes/anomalies')
def anomalies():
    """Detect process anomalies"""
    procs = get_process_tree()
    return jsonify({'anomalies': detect_anomalies(procs)})

@monitor_bp.route('/api/processes/<int:pid>/kill', methods=['POST'])
def kill_process(pid):
    """Kill a process"""
    try:
        p = psutil.Process(pid)
        name = p.name()
        p.kill()
        return jsonify({'success': True, 'killed': {'pid': pid, 'name': name}})
    except psutil.NoSuchProcess:
        return jsonify({'success': False, 'error': 'Process not found'}), 404
    except psutil.AccessDenied:
        return jsonify({'success': False, 'error': 'Access denied'}), 403

@monitor_bp.route('/api/processes/<int:pid>/info')
def process_info(pid):
    """Get detailed process info"""
    try:
        p = psutil.Process(pid)
        return jsonify({
            'pid': pid,
            'name': p.name(),
            'exe': p.exe(),
            'cwd': p.cwd(),
            'cmdline': p.cmdline(),
            'status': p.status(),
            'create_time': p.create_time(),
            'cpu_percent': p.cpu_percent(),
            'memory_info': dict(p.memory_info()._asdict()),
            'num_threads': p.num_threads(),
            'num_handles': p.num_handles() if hasattr(p, 'num_handles') else None,
            'connections': len(p.connections()),
            'open_files': len(p.open_files())
        })
    except psutil.NoSuchProcess:
        return jsonify({'error': 'Process not found'}), 404

@monitor_bp.route('/api/processes/by-name/<name>')
def processes_by_name(name):
    """Find processes by name"""
    procs = [p for p in get_process_tree() if name.lower() in p['name'].lower()]
    return jsonify({'processes': procs, 'count': len(procs)})
