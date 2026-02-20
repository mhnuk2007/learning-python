""" regex-pitfalls.py - Common Mistakes / Notes """

import re

# Overcomplicating simple string methods
simple_text = "Hello World"
# Instead of using regex to check start:
# re.match(r'^Hello', simple_text)
# Better: simple_text.startswith("Hello")
print("Starts with Hello:", simple_text.startswith("Hello"))

# Forgetting to escape special characters
pattern_wrong = r"3.14"  # '.' matches any character, not a literal dot
pattern_correct = r"3\.14"
print("3.14 match:", re.search(pattern_correct, "3.14") is not None)
