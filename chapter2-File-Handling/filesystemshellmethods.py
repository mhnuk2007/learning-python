import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile  # For working with zip archives

# Original file to work with
original_file = "example.txt"

# Check if the file exists
if path.exists(original_file):
    # Get absolute path of the original file
    src = path.realpath(original_file)
    print("Source file:", src)

    # Create a backup copy by appending ".bak" to the original filename
    backup_file = src + ".bak"
    shutil.copy(src, backup_file)
    print("Backup created:", backup_file)

    # Rename the original file
    renamed_file = "example_renamed.txt"
    os.rename(src, renamed_file)
    print("File renamed to:", renamed_file)

    # Create a ZIP archive of all files in the same directory
    root_dir = path.dirname(path.realpath(renamed_file))  # Get directory of the file
    make_archive("archive", "zip", root_dir)  # Archive all files in root_dir
    print("Archive created: archive.zip")

    # Create a custom ZIP archive with only the renamed and backup files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write(renamed_file)     # Add renamed file
        newzip.write(backup_file)      # Add backup file
    print("Custom ZIP created: testzip.zip")