import random

def generate_event():
    events = [
        {"type": "registry", "subtype": "autorun", "description": "Registry autorun created: HKCU\\Software\\...\\Run", "severity": "High"},
        {"type": "registry", "subtype": "changed", "description": "Registry changed: HKLM\\Software\\Vendor", "severity": "Medium"},
        {"type": "registry", "subtype": "permission", "description": "Registry permissions changed", "severity": "High"},
        {"type": "registry", "subtype": "audit", "description": "Audit policy modified", "severity": "Low"}
    ]
    return random.choice(events)

