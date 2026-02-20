""" simple-search.py - Simple Search with re.search() """

import re

text = "My phone number is 555-1234."
match = re.search(r'\d{3}-\d{4}', text)  # pattern: 3 digits, hyphen, 4 digits
if match:
    print("Found a phone number:", match.group())
else:
    print("No phone number found.")