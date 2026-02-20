""" csv-basics.py - Working with CSV """

import csv
from pathlib import Path

csv_path = Path("products.csv")
fieldnames = ["id", "name", "price"]

# write CSV
with csv_path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Laptop", "price": 1200})
    writer.writerow({"id": 2, "name": "Mouse", "price": 25})
    writer.writerow({"id": 3, "name": "Keyboard", "price": 45})

# read CSV
with csv_path.open("r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)