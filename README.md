# EDR Lab — Simulated Endpoint Detection & Response

This project is a **lightweight Endpoint Detection & Response (EDR) simulator** built in Python.  
It continuously monitors and generates alerts for **file, process, network, and registry events** —  
demonstrating how modern EDR systems work at a high level.

---

## 🚀 Features
- **File Monitoring** → Detects simulated file creation, modification, and deletion events.
- **Process Monitoring** → Logs suspicious process creation & termination events.
- **Network Monitoring** → Flags DNS queries and outbound/inbound connections.
- **Registry Monitoring** → Simulates autorun entries, permission changes, and policy modifications.
- **Alerting System** → Each event is tagged with type, severity, and timestamp.

---
## Project layout
edr-lab/
├── main.py # EDR Simulation <br>
├── modules/                 <br>
│ ├── event_logger.py        <br>
│ ├── process_monitor.py     <br>
│ ├── file_monitor.py        <br>
│ ├── network_monitor.py     <br>
│ └── registry_monitor.py    <br>
├── logs/                    <br>
└── README.md          

---

## ▶️ Usage
Clone the repo:
```bash
git clone https://github.com/ajaykr09/edr-lab.git
cd edr-lab

---

## Quick start
python3 main.py

Stop the demo with Ctrl+C.
Check logs/events.log for persisted events.

🎯 Why this project?

I built this project to learn and demonstrate security monitoring concepts.
It’s a great way to showcase knowledge of EDR, event logging, and threat detection. Feed simulated events to a SIEM pipeline. Extend detection logic into a real monitor (psutil/watchdog) for production-style labs.

Author

Ajay K — https://github.com/ajaykr09
