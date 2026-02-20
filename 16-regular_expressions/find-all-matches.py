""" find-all-matches.py - Find All Matches with re.findall() """

import re

text = "Call 555-1234 or 555-5678 for assistance."
numbers = re.findall(r'\d{3}-\d{4}', text)
print("All phone numbers found:", numbers)