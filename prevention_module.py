blocked_ips = set()

def block_ip(ip):
    blocked_ips.add(ip)
    print(f"[ALERT] Blocked IP: {ip}")

def is_blocked(ip):
    return ip in blocked_ips

def alert_admin(message):
    print(f"[ALERT] {message}")