""" Polling Example - Monitoring a Folder """

import time
from pathlib import Path

# Folder to monitor
folder = Path("monitor_folder")
folder.mkdir(exist_ok=True)

# Keep track of existing files
known_files = set(folder.iterdir())

print("Polling for new files...")

try:
    while True:
        current_files = set(folder.iterdir())
        new_files = current_files - known_files
        for f in new_files:
            print(f"New file detected: {f.name}")
        known_files = current_files
        time.sleep(2)  # wait before checking again
except KeyboardInterrupt:
    print("Polling stopped.")