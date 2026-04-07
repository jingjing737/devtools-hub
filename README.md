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
