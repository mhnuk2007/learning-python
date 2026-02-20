""" anchors.py - Anchors: Start (^) and End ($) """

import re

text = "Hello World"
if re.match(r"Hello", text):  # ^ implied at start
    print("Text starts with Hello")
if re.search(r"World$", text):
    print("Text ends with World")