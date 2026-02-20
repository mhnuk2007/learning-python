""" regex-split.py - Splitting with Regex """

import re

text = "apple, banana; cherry orange|pear"
fruits = re.split(r"[,;| ]+", text)  # split by comma, semicolon, pipe, or space
print("Fruits list:", fruits)