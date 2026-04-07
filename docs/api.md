# DevTools Hub API Documentation

## Base URL
```
http://localhost:5001/api
```

## Endpoints

### System Status
```bash
GET /api/status
```
Returns: CPU, Memory, Disk usage

### Process List
```bash
GET /api/processes?sort=cpu&limit=10
```
Returns: Top processes by CPU or Memory

### Network Info
```bash
GET /api/network
```
Returns: Network I/O statistics

### Disk Usage
```bash
GET /api/disk
```
Returns: Disk space info

### AI Commands
```bash
POST /api/ai
Content-Type: application/json

{
  "command": "查看系统状态"
}
```

## Example Response

```json
{
  "cpu": 45.2,
  "memory": 62.3,
  "disk": 71.5,
  "uptime": 1698723456
}
```
