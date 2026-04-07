"""端口和服务扫描"""
import socket
import subprocess

def scan_port(host, port, timeout=1):
    """扫描单个端口"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

def scan_common_ports(host="localhost"):
    """扫描常用端口"""
    common_ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3000: "Node.js",
        5000: "Flask",
        5001: "DevTools",
        5432: "PostgreSQL",
        6379: "Redis",
        8080: "Tomcat",
        8443: "HTTPS Alt",
        9000: "PHP-FPM",
        27017: "MongoDB"
    }
    results = []
    for port, name in common_ports.items():
        if scan_port(host, port):
            results.append({"port": port, "name": name, "status": "open"})
    return results

def get_services():
    """获取运行中的服务"""
    try:
        result = subprocess.run(
            ["launchctl", "list"],
            capture_output=True, text=True
        )
        services = []
        for line in result.stdout.split("\n")[1:20]:
            parts = line.split()
            if len(parts) >= 3:
                services.append({
                    "pid": parts[0],
                    "status": parts[1],
                    "name": parts[2]
                })
        return services
    except:
        return []
