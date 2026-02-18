from pathlib import Path
from datetime import datetime

# Create a Path object for the file
file_path = Path("pathutils.py")  # Replace with your file name

# Print OS-independent absolute path
print("File path:", file_path.resolve())

# Check if the file exists
print("Item exists:", file_path.exists())

# Check if it is a file or directory
print("Is it a file?", file_path.is_file())
print("Is it a directory?", file_path.is_dir())

# Get file size in bytes
if file_path.exists():
    print("Item size (bytes):", file_path.stat().st_size)

# Get last modification time
if file_path.exists():
    mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    print("Last modification time:", mod_time)

# Get current datetime in different formats
now = datetime.now()
print("Current time:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Date only:", now.strftime("%Y-%m-%d"))
print("Year only:", now.strftime("%Y"))

# Calculate time since last modification
if file_path.exists():
    time_since_mod = now - datetime.fromtimestamp(file_path.stat().st_mtime)
    print("Time since last modification:", time_since_mod)