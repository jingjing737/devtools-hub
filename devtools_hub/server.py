"""DevTools Hub Server"""
from flask import Flask, jsonify
import psutil
import platform

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/system")
def system():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "cpu_count": psutil.cpu_count()
    })

@app.route("/api/processes/top")
def processes_top():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procs.append(p.info)
        except:
            pass
    by_cpu = sorted(procs, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:10]
    by_mem = sorted(procs, key=lambda x: x['memory_percent'] or 0, reverse=True)[:10]
    return jsonify({"by_cpu": by_cpu, "by_memory": by_mem})

@app.route("/api/network/bandwidth")
def network():
    return jsonify({"upload_mbps": 0, "download_mbps": 0})

@app.route("/api/benchmark/full")
def benchmark():
    return jsonify({"cpu_score": 100, "total_score": 100})

if __name__ == "__main__":
    app.run(port=5001)
