""" raw-strings.py - Using Raw Strings for Patterns """

import re

# Without raw string, backslashes get confusing
path = r"C:\Users\Honey\Documents"
match_path = re.search(r"C:\\Users\\Honey", path)
if match_path:
    print("Path matched successfully!")