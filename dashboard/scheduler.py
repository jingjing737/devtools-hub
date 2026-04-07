"""Task Scheduler for automated tasks"""
from flask import Blueprint, jsonify, request
import threading
import time
import json
import os

scheduler_bp = Blueprint('scheduler', __name__)

SCHEDULE_FILE = '/tmp/.devtools_schedule.json'
scheduled_tasks = {}

def load_tasks():
    if os.path.exists(SCHEDULE_FILE):
        with open(SCHEDULE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_tasks(tasks):
    with open(SCHEDULE_FILE, 'w') as f:
        json.dump(tasks, f)

def run_task(task_id, task):
    """Execute a scheduled task"""
    print(f"Running task {task_id}: {task}")
    # Task execution logic here

@scheduler_bp.route('/api/scheduler/tasks')
def list_tasks():
    """List all scheduled tasks"""
    tasks = load_tasks()
    return jsonify({'tasks': tasks})

@scheduler_bp.route('/api/scheduler/tasks', methods=['POST'])
def create_task():
    """Create a new scheduled task"""
    data = request.json
    task_id = str(int(time.time()))
    tasks = load_tasks()
    tasks[task_id] = {
        'name': data.get('name'),
        'command': data.get('command'),
        'interval': data.get('interval'),  # seconds
        'last_run': None,
        'enabled': True
    }
    save_tasks(tasks)
    return jsonify({'task_id': task_id, 'task': tasks[task_id]})

@scheduler_bp.route('/api/scheduler/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a scheduled task"""
    tasks = load_tasks()
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Task not found'}), 404

@scheduler_bp.route('/api/scheduler/tasks/<task_id>/run', methods=['POST'])
def run_task_now(task_id):
    """Run a task immediately"""
    tasks = load_tasks()
    if task_id in tasks:
        run_task(task_id, tasks[task_id])
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Task not found'}), 404
