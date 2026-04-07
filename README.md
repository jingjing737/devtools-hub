# DevTools Hub 🔧

> A developer toolbox with system monitoring, process management, and AI integration.

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/github/license/jingjing737/devtools-hub)](LICENSE)

## Features

### 📊 Dashboard
- Real-time system monitoring (CPU, Memory, Disk)
- Process management
- Network statistics
- Dark theme UI

### 🤖 AI Integration
- Natural language commands
- Smart system queries
- Voice-ready API endpoints

### ⚡ CLI Tools
- Quick system status
- Process management
- Log viewing
- File backup

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
python dashboard/app.py

# Run AI API
python dashboard/ai_api.py

# Use CLI
python cli/manager.py status
python cli/manager.py processes
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/status` | System status |
| `/api/processes` | Process list |
| `/api/disk` | Disk usage |
| `/api/memory` | Memory usage |
| `/api/network` | Network stats |
| `/api/ai` | AI command interface |

## Screenshots

![Dashboard](docs/dashboard.png)

## Project Structure

```
devtools-hub/
├── dashboard/       # Web dashboard
│   ├── app.py      # Main Flask app
│   ├── ai_api.py   # AI endpoints
│   └── templates/  # HTML templates
├── cli/            # Command line tools
│   └── manager.py  # System manager CLI
├── docs/           # Documentation
└── requirements.txt
```

## Requirements

- Python 3.9+
- Flask
- psutil
- psutil (for system monitoring)

## License

MIT License - feel free to use!

## New Features (v2.0)

### 🤖 AI Integration
- OpenAI GPT-4 integration
- Claude 3 integration
- Local LLM support (Ollama)
- Auto-code review
- Smart error analysis

### 📊 Enhanced Dashboard
- Real-time system monitoring
- Process management with AI insights
- Resource usage predictions
- Anomaly detection alerts

### 🔧 Developer Tools
- Git repository status
- Docker container management
- Database connections
- API testing tools
- Log analysis

### 🚀 Performance
- Async operations
- Caching layer
- Rate limiting
- WebSocket support

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/system | GET | System info |
| /api/processes | GET | Process list |
| /api/processes/:pid | DELETE | Kill process |
| /api/ai/chat | POST | AI chat |
| /api/ai/analyze | POST | Code analysis |
| /api/git/status | GET | Git status |
| /api/docker/ps | GET | Docker containers |

## Configuration

```python
# config.py
OPENAI_API_KEY = "your-key"
CLAUDE_API_KEY = "your-key"
OLLAMA_BASE_URL = "http://localhost:11434"
```

## Docker Support

```bash
# Build
docker build -t devtools-hub .

# Run
docker run -p 5001:5001 devtools-hub
```

## Screenshots

(Coming soon)

## Roadmap

- [ ] Kubernetes integration
- [ ] Multi-server monitoring
- [ ] Custom dashboards
- [ ] Plugin system
- [ ] Mobile app

## Contributing

PRs welcome! See CONTRIBUTING.md

## License

MIT

## 📦 Releases

| Version | Date | Changes |
|---------|------|---------|
| v2.0.0 | 2026-04-07 | AI integration, enhanced dashboard, API endpoints |
| v1.0.0 | 2026-04-07 | Initial release |

### Changelog

#### v2.0.0 (2026-04-07)
- ✨ OpenAI GPT-4 integration
- ✨ Claude 3 integration
- ✨ Local LLM support (Ollama)
- ✨ Real-time system monitoring
- ✨ Process management with AI insights
- ✨ Docker support
- 📝 Full REST API

#### v1.0.0 (2026-04-07)
- 🎉 Initial release
- ✨ Basic system monitoring
- ✨ Process management

## 📦 Packages

### pip
```bash
pip install devtools-hub
```

### Docker
```bash
docker pull ghcr.io/jingjing737/devtools-hub:latest
docker run -p 5001:5001 ghcr.io/jingjing737/devtools-hub
```

### From Source
```bash
git clone https://github.com/jingjing737/devtools-hub.git
cd devtools-hub
pip install -r requirements.txt
python dashboard/app.py
```

### Quick Start
```bash
# Install
pip install devtools-hub

# Run
devtools-hub --port 5001

# Open
open http://localhost:5001
```

## 🔄 Auto-Update

This repository is automatically updated hourly.

Last update: 2026-04-07 14:38 GMT+8

## 🏥 Health Check API

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/health | GET | Full system health |
| /api/health/cpu-history | GET | CPU usage samples |
| /api/health/services | GET | Service status check |
| /api/health/battery | GET | Battery info |

### Example Response

```json
{
  "status": "healthy",
  "system": {
    "platform": "Darwin",
    "uptime": "5d 12h",
    "cpu_cores_logical": 8
  },
  "memory": {
    "total_gb": 16.0,
    "available_gb": 6.2,
    "percent": 61.2
  },
  "disk": {
    "write_speed_mbps": 245.3,
    "read_speed_mbps": 312.8
  }
}
```

## 🐳 Docker Commands

```bash
# Build
docker build -t devtools-hub .

# Run
docker run -d -p 5001:5001 --name devtools devtools-hub

# Compose
docker-compose up -d

# Logs
docker logs -f devtools

# Stop
docker-compose down
```

## 🧪 Testing

```bash
# Run tests
python test_api.py

# Health check
curl http://localhost:5001/api/health

# CPU history
curl http://localhost:5001/api/health/cpu-history

# Service status
curl http://localhost:5001/api/health/services
```

## 📁 Project Structure

```
devtools-hub/
├── dashboard/
│   ├── app.py           # Main Flask app
│   ├── api.py           # System API
│   ├── health_api.py    # Health check API
│   └── templates/
│       └── index.html   # Dashboard UI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

**Last Updated**: 2026-04-07 14:41 GMT+8

## 🔍 Advanced Monitoring APIs

### Process Monitor
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/processes/tree | GET | Full process tree |
| /api/processes/top | GET | Top CPU/memory processes |
| /api/processes/anomalies | GET | Detect anomalies |
| /api/processes/:pid/info | GET | Detailed process info |
| /api/processes/:pid/kill | POST | Kill process |
| /api/processes/by-name/:name | GET | Find by name |

### Network Monitor
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/network/bandwidth | GET | Real-time bandwidth |
| /api/network/interfaces | GET | Network interfaces |
| /api/network/connections | GET | Active connections |
| /api/network/stats | GET | Network statistics |

### Example: Bandwidth Response
```json
{
  "upload_mbps": 12.5,
  "download_mbps": 85.3,
  "upload_bps": 1562500,
  "download_bps": 10662500
}
```

### Example: Top Processes
```json
{
  "by_cpu": [
    {"pid": 1234, "name": "python", "cpu": 45.2, "memory": 12.3}
  ],
  "by_memory": [
    {"pid": 5678, "name": "chrome", "cpu": 5.1, "memory": 28.7}
  ],
  "total": 245
}
```

## 🔌 AI Integration

### OpenAI
```python
import openai
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Analyze this process"}]
)
```

### Claude
```python
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-5-sonnet",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Analyze system"}]
)
```

### Ollama (Local)
```python
import requests
response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": "Analyze processes"}
)
```

## 📊 Dashboard Preview

```
┌─────────────────────────────────────────────────┐
│  DevTools Hub v2.2.0                            │
├─────────────────────────────────────────────────┤
│  CPU: ████████░░ 78%    │  Memory: ██████░░░░ 62% │
│  Disk: ███░░░░░░░ 35%   │  Network: ↓85 ↑12 Mbps │
├─────────────────────────────────────────────────┤
│  Top Processes:                                 │
│  • python (45%) - AI inference                  │
│  • chrome (28%) - Browser                       │
│  • docker (12%) - Containers                    │
└─────────────────────────────────────────────────┘
```

---

**Version**: v2.2.0
**Last Updated**: 2026-04-07 14:46 GMT+8
