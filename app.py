from flask import Flask, render_template
from detection_engine import detect_attack
from prevention_module import block_ip, alert_admin, blocked_ips
from database import get_logs, log_packet

import threading
import random
import time
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    logs = get_logs()

    alerts = []
    total_attacks = 0

    for log in logs:
        if "⚠" in log[3]:
            alerts.append(log)
            total_attacks += 1

    return render_template(
        "index.html",
        logs=logs,
        alerts=alerts[:10],
        total_logs=len(logs),
        total_attacks=total_attacks,
        blocked_count=len(blocked_ips)
    )


def monitor():
    ips = ["192.168.1.10","192.168.1.12","192.168.1.15","10.0.0.5","172.16.0.3"]
    destinations = ["192.168.1.1","192.168.1.2","192.168.1.3"]
    protocols = ["TCP","UDP","HTTP","HTTPS"]

    while True:
        src_ip = random.choice(ips)
        dst_ip = random.choice(destinations)
        base_protocol = random.choice(protocols)
        timestamp = datetime.now()

        attack = detect_attack(src_ip)

        if attack:
            protocol = f"{base_protocol} | ⚠ {attack}"
            block_ip(src_ip)
            alert_admin(f"{attack} detected from {src_ip}")
        else:
            protocol = base_protocol

        log_packet(src_ip, dst_ip, protocol, timestamp)

        time.sleep(1)


if __name__ == "__main__":
    t = threading.Thread(target=monitor)
    t.daemon = True
    t.start()

    app.run(debug=True)