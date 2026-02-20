""" pathlib-paths.py - Using pathlib for Paths """

from pathlib import Path

base_dir = Path("my_project")  # relative path
sub_dir = base_dir / "data"
sub_dir.mkdir(parents=True, exist_ok=True)  # create directories if missing

file_in_subdir = sub_dir / "example.txt"
file_in_subdir.write_text("Hello, this is a test file.")

print("File exists?", file_in_subdir.exists())
print("File content:", file_in_subdir.read_text())