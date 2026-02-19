import os                   # Provides functions to interact with the operating system
from os import path          # Contains utilities to handle file paths
import datetime              # For working with dates and times
from datetime import date, time, timedelta  # Specific date/time classes
import time                  # For working with timestamps and delays

# Print the name of the operating system
# 'nt' = Windows, 'posix' = Linux/macOS
print(os.name)

# Print the current working directory
print(os.getcwd())

# List all files and directories in the current directory
print(os.listdir())

# Check if a specific file exists
print("Item exists:", path.exists("pathutils.py"))

# Check if the item is a file
print("Is it a file?", path.isfile("pathutils.py"))

# Check if the item is a directory
print("Is it a directory?", path.isdir("pathutils.py"))

# Get the size of the file in bytes
print("Item size:", path.getsize("pathutils.py"))

# Get the absolute path of the file
print("Item path:", path.realpath("pathutils.py"))

# Split the absolute path into directory and filename
print("Item path and name:", path.split(path.realpath("pathutils.py")))

# Get the last modification time as a timestamp
print("Item modification time:", path.getmtime("pathutils.py"))

# Convert the timestamp to a human-readable datetime
print("Item modification time:", datetime.datetime.fromtimestamp(path.getmtime("pathutils.py")))

# Display the current date and time in different formats
print("Current time:", datetime.datetime.now())
print("Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
print("Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H"))
print("Current time:", datetime.datetime.now().strftime("%Y-%m-%d"))
print("Current time:", datetime.datetime.now().strftime("%Y"))

# Calculate time elapsed since last modification of the file
if path.exists("example.txt"):  # Ensure the file exists to avoid errors
    mod_time = path.getmtime("example.txt")  # Get modification timestamp
    current_time = datetime.datetime.now()   # Get current datetime
    # Calculate timedelta between now and last modification
    time_since_mod = current_time - datetime.datetime.fromtimestamp(mod_time)
    print("Time since last modification:", time_since_mod)