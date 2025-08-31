# EDR Lab — Simulated Endpoint Detection & Response

Simulated EDR monitoring environment built in Python. Tracks file, process, network, and registry events with real-time alerts.

---

## 🗂 Project Layout

edr-lab/ <br>
├── main.py <br>
├── modules/ <br> 
│ ├── event_logger.py <br>
│ ├── process_monitor.py <br>
│ ├── file_monitor.py <br>
│ ├── network_monitor.py <br> 
│ └── registry_monitor.py <br> 
├── logs/<br> 
└── README.md <br>

---

## ⚡ Features

- **File Monitoring** – Detects file creation, modification, deletion.
- **Process Monitoring** – Tracks process start and stop events.
- **Network Simulation** – Logs simulated network connections.
- **Registry Simulation** – Monitors registry-like events for demonstration.
- **Real-Time Alerts** – JSON-formatted alerts printed to console.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/ajaykr09/edr-lab.git
cd edr-lab

3. Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

6. Run the EDR agent:
python3 main.py

5. In a separate terminal, run demo scripts to generate events:
python3 test_edr_events_demo.py
Press Ctrl+C to stop the agent.

💻 Technology Stack
Python 3

psutil for process monitoring

watchdog for file system monitoring

JSON for alert logging

📈 Usage
This is a simulated environment designed for educational purposes, ideal for understanding how EDR agents track endpoint activity.
