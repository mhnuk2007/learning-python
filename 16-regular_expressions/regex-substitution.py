""" regex-substitution.py - Replace/Substitution with re.sub() """

import re

text = "Hello Alice, hello Bob."
# Replace 'hello' (case-insensitive) with 'hi'
new_text = re.sub(r'hello', 'hi', text, flags=re.IGNORECASE)
print("Replaced text:", new_text)