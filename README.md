# Smart Intrusion Detection and Prevention System (IDPS)

A comprehensive, real-time network security monitoring system designed to detect and prevent intrusion attempts, particularly Denial of Service (DoS) attacks. Built with Python and Flask, this system provides a web-based dashboard for security operations center (SOC) monitoring.

## 🚀 Features

### Core Security Capabilities
- **Real-time Traffic Monitoring**: Continuous monitoring of network packets with live logging
- **DoS Attack Detection**: Intelligent detection of Denial of Service attacks based on configurable thresholds
- **Automatic IP Blocking**: Immediate blocking of malicious IP addresses upon attack detection
- **Alert System**: Real-time notifications for security incidents
- **Web Dashboard**: Modern, responsive interface for security monitoring

### Dashboard Features
- **Key Performance Indicators (KPIs)**:
  - Total network traffic count
  - Detected attack statistics
  - Blocked IP addresses count
- **Live Traffic Stream**: Real-time display of network events
- **Alert Panel**: Recent security alerts with timestamps
- **Auto-refresh**: Dashboard updates every 3 seconds for real-time monitoring

### Technical Features
- **SQLite Database**: Persistent logging of all network events
- **Multi-threaded Architecture**: Concurrent monitoring and web serving
- **Packet Sniffing**: Integration with Scapy for actual network packet capture
- **Simulation Mode**: Built-in traffic simulation for testing and demonstration

## 🏗️ Architecture

The system consists of several modular components:

- **`app.py`**: Main Flask application and web server
- **`detection_engine.py`**: Core intrusion detection logic
- **`prevention_module.py`**: IP blocking and alert management
- **`database.py`**: SQLite database operations for logging
- **`traffic_monitor.py`**: Packet sniffing functionality using Scapy
- **`templates/index.html`**: Web dashboard template
- **`static/style.css`**: Dashboard styling

## 📋 Prerequisites

- Python 3.7+
- Linux/Unix environment (for packet sniffing capabilities)
- Root privileges (for network packet capture)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vbhhacl/Smart-Intrusion-Detection-Prevention-System-IDPS-.git
   cd Smart-Intrusion-Detection-Prevention-System-IDPS-
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   The database will be automatically created when you first run the application.

## 🚀 Usage

### Running in Simulation Mode

For testing and demonstration purposes, the system includes a built-in traffic simulator:

```bash
python app.py
```

This will start the web server on `http://localhost:5000` with simulated network traffic.

### Running with Real Packet Sniffing

For production use with actual network monitoring:

1. Ensure you have root privileges
2. Modify `app.py` to use `traffic_monitor.py` instead of the simulation loop
3. Run with elevated privileges:

```bash
sudo python app.py
```

### Accessing the Dashboard

Once running, access the security dashboard at: `http://localhost:5000`

The dashboard displays:
- Real-time network traffic
- Security alerts
- Blocked IP addresses
- Attack statistics

## ⚙️ Configuration

### Detection Parameters

Modify thresholds in `detection_engine.py`:

```python
THRESHOLD_DOS = 20  # Number of requests before DoS detection
```

### Network Interfaces

For packet sniffing, configure the network interface in `traffic_monitor.py`:

```python
sniff(iface="eth0", prn=process_packet, store=False)
```

## 🔍 How It Works

1. **Traffic Monitoring**: The system continuously monitors network packets
2. **Attack Detection**: Each packet is analyzed against predefined security rules
3. **Prevention**: Upon detecting an attack, the malicious IP is automatically blocked
4. **Logging**: All events are logged to the SQLite database
5. **Alerting**: Security administrators are notified of incidents
6. **Dashboard**: Real-time visualization of security status

### Detection Logic

The current implementation focuses on DoS attack detection using:
- Request frequency analysis
- Threshold-based blocking
- IP-based tracking

## 🛡️ Security Considerations

- Run with minimal privileges in production
- Regularly update dependencies
- Monitor system performance under high traffic
- Implement proper logging rotation
- Consider integrating with external security systems

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Advanced attack pattern recognition (DDoS, SQL injection, XSS)
- [ ] Machine learning-based anomaly detection
- [ ] Integration with SIEM systems
- [ ] RESTful API for external integrations
- [ ] Multi-interface support
- [ ] Alert escalation and notification systems
- [ ] Historical analytics and reporting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Vbhhacl** - *Initial work* - [GitHub](https://github.com/Vbhhacl)

## 🙏 Acknowledgments

- Flask framework for web development
- Scapy for network packet manipulation
- Open source security community

---

**Note**: This is a demonstration and educational project. For production use, consider professional security solutions and thorough security audits.