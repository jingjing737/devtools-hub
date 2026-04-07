"""
DevTools Hub Dashboard
A web-based control panel for developer tools.
"""

from flask import Flask, render_template, jsonify, request
import psutil
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sysinfo')
def sysinfo():
    return jsonify({
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'uptime': get_uptime()
    })

@app.route('/api/processes')
def processes():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procs.append({
                'pid': p.info['pid'],
                'name': p.info['name'],
                'cpu': p.info['cpu_percent'],
                'memory': p.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return jsonify(procs[:20])

@app.route('/api/git/status')
def git_status():
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd=os.getcwd())
        return jsonify({'status': result.stdout or 'clean'})
    except Exception as e:
        return jsonify({'status': str(e)})

def get_uptime():
    boot_time = psutil.boot_time()
    import time
    uptime = int(time.time() - boot_time)
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    return f"{hours}h {minutes}m"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)