""" capture-groups.py - Capture Groups for Extracting Parts """

import re

text = "Order number: 12345, Date: 2026-02-20"
pattern = r"Order number: (\d+), Date: (\d{4}-\d{2}-\d{2})"
match = re.search(pattern, text)
if match:
    order_number, date = match.groups()
    print("Order number:", order_number)
    print("Date:", date)