#!/usr/bin/env python3
"""
EDR Lab - main entrypoint
Runs simple simulated monitors and logs events.
"""
import time
from modules import process_monitor, file_monitor, network_monitor, registry_monitor, event_logger

def main():
    print("=== EDR Lab — Simulated Monitoring ===")
    print("Press Ctrl+C to stop.\n")

    logger = event_logger.EventLogger("logs/events.log", jsonl=True)

    try:
        while True:
            # rotate through monitors
            ev = process_monitor.generate_event()
            logger.log_event(ev)

            ev = file_monitor.generate_event()
            logger.log_event(ev)

            ev = network_monitor.generate_event()
            logger.log_event(ev)

            ev = registry_monitor.generate_event()
            logger.log_event(ev)

            time.sleep(1)  # adjust speed for demo
    except KeyboardInterrupt:
        print("\n[INFO] Stopped by user.")

if __name__ == "__main__":
    main()

