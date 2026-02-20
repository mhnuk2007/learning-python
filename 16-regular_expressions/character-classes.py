""" character-classes.py - Character Classes [] """

import re

text = "My email addresses are alice@example.com and bob_123@domain.org"
emails = re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z]+\.(com|org|net)", text)
print("Emails found:", emails)