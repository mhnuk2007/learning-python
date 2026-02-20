""" quantifiers.py - Quantifiers {n}, {n,m}, *, +, ? """

import re

text = "There are 1, 12, 123, and 1234 items."
matches = re.findall(r'\d{2,3}', text)  # match 2 or 3 digits
print("2-3 digit numbers:", matches)