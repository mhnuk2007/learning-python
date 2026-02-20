""" file-pitfalls.py - Common Mistakes """

import csv
from pathlib import Path

# Mixing numeric and string types in CSV
bad_csv_path = Path("bad.csv")
with bad_csv_path.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "price"])
    writer.writerow([1, 25])          # int
    writer.writerow([2, "45"])        # str (inconsistent)
# Better: keep consistent types

print("CSV written with inconsistent types - avoid this in production!")