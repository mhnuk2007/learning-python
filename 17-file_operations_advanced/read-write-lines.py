""" read-write-lines.py - Reading/Writing Multiple Lines """

from pathlib import Path

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file_lines = Path("lines.txt")

# write lines
with file_lines.open("w") as f:
    f.writelines(lines)

# read lines
with file_lines.open("r") as f:
    for line in f:
        print("Read line:", line.strip())