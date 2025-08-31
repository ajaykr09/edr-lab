import random

def generate_event():
    events = [
        {"type": "file", "subtype": "created", "description": "File created: invoice.docx", "severity": "Medium"},
        {"type": "file", "subtype": "modified", "description": "File modified: secret.xlsx", "severity": "High"},
        {"type": "file", "subtype": "deleted", "description": "File deleted: report.pdf", "severity": "High"},
        {"type": "file", "subtype": "modified", "description": "File modified: notes.txt", "severity": "Low"}
    ]
    return random.choice(events)

