""" json-append.py - Appending JSON to a List """

import json
from pathlib import Path

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

users_path = Path("users.json")
with users_path.open("w") as f:
    json.dump(users, f, indent=2)

# read and append a new user
with users_path.open("r+") as f:
    current_users = json.load(f)
    current_users.append({"name": "Charlie", "age": 28})
    f.seek(0)
    json.dump(current_users, f, indent=2)
    f.truncate()  # remove leftover old data
print("Updated users list:", current_users)