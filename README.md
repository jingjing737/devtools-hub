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
