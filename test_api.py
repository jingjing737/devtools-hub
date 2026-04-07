#!/usr/bin/env python3
"""Quick test script for DevTools Hub API"""
import requests
import json

BASE = "http://localhost:5001/api"

def test_status():
    r = requests.get(f"{BASE}/status")
    print("Status:", r.json())

def test_processes():
    r = requests.get(f"{BASE}/processes?limit=5")
    print("Processes:", json.dumps(r.json()[:2], indent=2))

def test_ai():
    r = requests.post(f"{BASE}/ai", json={"command": "内存使用"})
    print("AI:", r.json())

if __name__ == "__main__":
    test_status()
    test_processes()
    test_ai()
