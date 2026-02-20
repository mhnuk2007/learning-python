"""Advanced file operations demo using JSON and CSV."""

from __future__ import annotations

import csv
import json
from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    out_dir = base_dir / "artifacts"
    out_dir.mkdir(exist_ok=True)

    users = [
        {"id": 1, "name": "Asha", "score": 92},
        {"id": 2, "name": "Ben", "score": 88},
    ]

    json_path = out_dir / "users.json"
    csv_path = out_dir / "users.csv"

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "score"])
        writer.writeheader()
        writer.writerows(users)

    with json_path.open("r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("Wrote:", json_path)
    print("Wrote:", csv_path)
    print("Loaded users:", loaded)


if __name__ == "__main__":
    main()
