"""System Log Analyzer"""
from flask import Blueprint, jsonify
import subprocess
import re

log_bp = Blueprint('log', __name__)

@log_bp.route('/api/logs/errors')
def recent_errors():
    """Get recent system errors (macOS)"""
    try:
        result = subprocess.run(
            ['log', 'show', '--predicate', 'messageType == error', 
             '--last', '1h', '--style', 'compact'],
            capture_output=True, text=True, timeout=10
        )
        lines = result.stdout.strip().split('\n')[-20:]
        return jsonify({'errors': lines, 'count': len(lines)})
    except Exception as e:
        return jsonify({'error': str(e)})

@log_bp.route('/api/logs/kernel')
def kernel_messages():
    """Get kernel messages"""
    try:
        result = subprocess.run(
            ['log', 'show', '--predicate', 'subsystem == "com.apple.kernel"',
             '--last', '1h', '--style', 'compact'],
            capture_output=True, text=True, timeout=10
        )
        lines = result.stdout.strip().split('\n')[-20:]
        return jsonify({'messages': lines})
    except Exception as e:
        return jsonify({'error': str(e)})

@log_bp.route('/api/logs/apps')
def app_crashes():
    """Get recent app crashes"""
    try:
        result = subprocess.run(
            ['log', 'show', '--predicate', 'eventMessage CONTAINS "crashed"',
             '--last', '24h', '--style', 'compact'],
            capture_output=True, text=True, timeout=10
        )
        lines = result.stdout.strip().split('\n')[-10:]
        return jsonify({'crashes': lines})
    except Exception as e:
        return jsonify({'error': str(e)})
