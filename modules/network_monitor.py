import random

def generate_event():
    events = [
        {"type": "network", "subtype": "connection", "description": "Outgoing connection to 192.0.2.10:443", "severity": "Medium"},
        {"type": "network", "subtype": "connection", "description": "Outgoing connection to 203.0.113.5:8080", "severity": "High"},
        {"type": "network", "subtype": "dns", "description": "DNS query for suspicious-domain.example", "severity": "High"},
        {"type": "network", "subtype": "connection", "description": "Local LAN connection to 10.0.0.5:22", "severity": "Low"}
    ]
    return random.choice(events)
