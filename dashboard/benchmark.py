"""System Benchmark Tool"""
from flask import Blueprint, jsonify
import time
import psutil
import subprocess
import hashlib

bench_bp = Blueprint('benchmark', __name__)

@bench_bp.route('/api/benchmark/cpu')
def cpu_benchmark():
    """CPU performance test"""
    start = time.time()
    # Fibonacci calculation
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    fib(35)
    elapsed = time.time() - start
    
    # Hash calculation
    start = time.time()
    for _ in range(100000):
        hashlib.sha256(b"test").hexdigest()
    hash_time = time.time() - start
    
    return jsonify({
        'fibonacci_35_time': round(elapsed, 3),
        'hash_100k_time': round(hash_time, 3),
        'cpu_score': round(1000 / (elapsed + hash_time), 1)
    })

@bench_bp.route('/api/benchmark/memory')
def memory_benchmark():
    """Memory performance test"""
    start = time.time()
    # Create large list
    data = [i for i in range(10000000)]
    create_time = time.time() - start
    
    start = time.time()
    # Sort
    sorted_data = sorted(data[:1000000])
    sort_time = time.time() - start
    
    del data, sorted_data
    
    return jsonify({
        'list_create_time': round(create_time, 3),
        'sort_time': round(sort_time, 3),
        'memory_score': round(1000 / (create_time + sort_time), 1)
    })

@bench_bp.route('/api/benchmark/disk')
def disk_benchmark():
    """Disk I/O benchmark"""
    test_file = '/tmp/.bench_test'
    data = b'0' * (100 * 1024 * 1024)  # 100MB
    
    # Write test
    start = time.time()
    with open(test_file, 'wb') as f:
        f.write(data)
    write_time = time.time() - start
    write_speed = len(data) / write_time / (1024**2)
    
    # Read test
    start = time.time()
    with open(test_file, 'rb') as f:
        f.read()
    read_time = time.time() - start
    read_speed = len(data) / read_time / (1024**2)
    
    import os
    os.remove(test_file)
    
    return jsonify({
        'write_speed_mbps': round(write_speed, 1),
        'read_speed_mbps': round(read_speed, 1),
        'write_time': round(write_time, 3),
        'read_time': round(read_time, 3),
        'disk_score': round((write_speed + read_speed) / 2, 1)
    })

@bench_bp.route('/api/benchmark/full')
def full_benchmark():
    """Run all benchmarks"""
    cpu = cpu_benchmark().get_json()
    memory = memory_benchmark().get_json()
    disk = disk_benchmark().get_json()
    
    total_score = cpu['cpu_score'] + memory['memory_score'] + disk['disk_score']
    
    return jsonify({
        'cpu': cpu,
        'memory': memory,
        'disk': disk,
        'total_score': round(total_score, 1),
        'timestamp': time.time()
    })
