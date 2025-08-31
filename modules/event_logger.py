import os
import json
from datetime import datetime

class EventLogger:
    def __init__(self, filepath='logs/events.log', jsonl=False):
        self.filepath = filepath
        self.jsonl = jsonl
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log_event(self, event: dict):
        event_out = event.copy()
        event_out['timestamp'] = self._timestamp()
        # Print friendly output
        print(f"[ALERT] {event_out}")
        # Persist: JSON lines if requested, else plain text
        with open(self.filepath, "a", encoding="utf-8") as f:
            if self.jsonl:
                f.write(json.dumps(event_out) + "\n")
            else:
                f.write(f"{event_out['timestamp']} - {event_out.get('type','')} - {event_out.get('description','')}\n")

