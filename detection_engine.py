from collections import defaultdict
import time

request_count = defaultdict(int)
failed_logins = defaultdict(int)

THRESHOLD_DOS = 20
THRESHOLD_BRUTE = 5

def detect_attack(ip):
    request_count[ip] += 1

    if request_count[ip] > THRESHOLD_DOS:
        return "DoS Attack"

    return None

def detect_bruteforce(ip):
    failed_logins[ip] += 1

    if failed_logins[ip] > THRESHOLD_BRUTE:
        return "Brute Force Attack"

    return None

def reset_counts():
    global request_count, failed_logins
    request_count.clear()
    failed_logins.clear()