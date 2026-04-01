from flask import Flask, render_template
from detection_engine import detect_attack
from prevention_module import block_ip, alert_admin
from database import get_logs, log_packet

import threading
import random
import time
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Dashboard Route
# -----------------------------
@app.route("/")
def dashboard():
    logs = get_logs()
    return render_template("index.html", logs=logs)


# -----------------------------
# Simulated Traffic Generator
# -----------------------------
def monitor():

    print("Traffic monitoring started (simulation mode)...")

    # Example IP pool
    ips = [
        "192.168.1.10",
        "192.168.1.12",
        "192.168.1.15",
        "10.0.0.5",
        "172.16.0.3"
    ]

    destinations = [
        "192.168.1.1",
        "192.168.1.2",
        "192.168.1.3"
    ]

    protocols = [
        "TCP",
        "UDP",
        "HTTP",
        "HTTPS"
    ]

    while True:

        # Random traffic generation
        src_ip = random.choice(ips)
        dst_ip = random.choice(destinations)
        protocol = random.choice(protocols)
        timestamp = datetime.now()

        # Store packet log
        log_packet(src_ip, dst_ip, protocol, timestamp)

        # Detect attacks
        attack = detect_attack(src_ip)

        if attack:
            block_ip(src_ip)
            alert_admin(f"{attack} detected from {src_ip}")

        # Print traffic in terminal
        print(f"Traffic: {src_ip} → {dst_ip} | {protocol}")

        # Traffic speed
        time.sleep(1)


# -----------------------------
# Run Flask + Monitor Thread
# -----------------------------
if __name__ == "__main__":

    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.daemon = True
    monitor_thread.start()

    app.run(debug=True)