""" json-basics.py - Working with JSON """

import json
from pathlib import Path

data = {
    "name": "Honey",
    "age": 19,
    "skills": ["Python", "Java", "React"],
    "is_student": True
}

# save JSON to file
json_path = Path("data.json")
with json_path.open("w") as f:
    json.dump(data, f, indent=4)  # pretty-print with indent

# read JSON from file
with json_path.open("r") as f:
    loaded_data = json.load(f)
print("Loaded JSON data:", loaded_data)