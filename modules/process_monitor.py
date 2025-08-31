import random

def generate_event():
    events = [
        {"type": "process", "subtype": "creation", "description": "Process created: notepad.exe", "severity": "Medium"},
        {"type": "process", "subtype": "creation", "description": "Process created: powershell.exe", "severity": "High"},
        {"type": "process", "subtype": "termination", "description": "Process terminated: updater.exe", "severity": "Low"},
        {"type": "process", "subtype": "creation", "description": "Suspicious process started: unknown_bin", "severity": "High"}
    ]
    return random.choice(events)
