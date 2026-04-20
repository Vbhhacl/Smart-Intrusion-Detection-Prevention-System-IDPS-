from collections import defaultdict

request_count = defaultdict(int)

THRESHOLD_DOS = 20

blocked_ips = set()

def detect_attack(ip):
    if ip in blocked_ips:
        return None

    request_count[ip] += 1

    if request_count[ip] > THRESHOLD_DOS:
        blocked_ips.add(ip)
        return "DoS Attack"

    return None