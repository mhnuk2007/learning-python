""" optional-alternation.py - Optional (?) and Alternation (|) """

import re

text = "I like cats, dogs, and birds."
matches = re.findall(r"cat|dog", text)  # match 'cat' or 'dog'
print("Animals found:", matches)

# Optional 's' at the end of 'dog'
text2 = "dog dogs dog dog"
matches2 = re.findall(r"dogs?", text2)
print("Optional 's' matched:", matches2)