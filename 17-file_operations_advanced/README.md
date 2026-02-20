# Chapter 17: File Operations Advanced

Advanced file workflows and data serialization.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of basic file handling (Chapter 02)
- Understanding of dictionaries (Chapter 11)

## How to run

```powershell
cd 17-file_operations_advanced
python .\json-basics.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `json-basics.py` | `json.dump()` and `json.load()` for JSON files |
| `json-append.py` | Appending to JSON list with `seek()` and `truncate()` |
| `csv-basics.py` | `csv.DictWriter` and `csv.DictReader` for CSV files |
| `pathlib-paths.py` | Using `pathlib.Path` for cross-platform paths |
| `read-write-lines.py` | Reading and writing multiple lines |
| `file-pitfalls.py` | Common mistakes and best practices |
| `json-csv-demo.py` | Original comprehensive examples |

## Key concepts

### JSON Operations

```python
import json
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    data = json.load(f)
```

### CSV Operations

```python
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name"])
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Alice"})

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

### pathlib Paths

```python
from pathlib import Path
path = Path("dir") / "subdir" / "file.txt"
path.mkdir(parents=True, exist_ok=True)
path.write_text("Hello")
content = path.read_text()
```

## Notes

- Use `indent` parameter for pretty-printed JSON
- Use `newline=""` when opening CSV files on Windows
- `pathlib` is preferred over `os.path` for modern Python
- Keep data types consistent in CSV files
- Use context managers (`with`) for automatic file closing

## Artifacts

- `artifacts/users.csv` - Sample CSV file
- `artifacts/users.json` - Sample JSON file

## Theory Notes

- [`17-file_operations_advanced.md`](17-file_operations_advanced.md)