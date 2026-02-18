# Chapter 2: File Handling

This chapter covers working with files, paths, and file system operations in Python.

## Prerequisites

- Python 3.x
- Run scripts from inside this folder:

```powershell
cd chapter2-File-Handling
```

## Files and topics

| File | Focus |
| --- | --- |
| `filehandling1.py` | Reading files with `readline()`, `readlines()`, `seek()` |
| `filehandling2.py` | Writing lines to a file, then reading and printing them |
| `pathutils.py` | `os` and `os.path` utilities: existence checks, metadata, timestamps |
| `pathutils-pathlib.py` | `pathlib.Path` version of common path/file operations |
| `filesystemshellmethods.py` | Copy, rename, and archive files (`shutil`, `zipfile`) |
| `challege-solution.py` | Challenge: total byte size of `.txt` files in `deps/` |

## Important notes

- `filehandling1.py` and `filesystemshellmethods.py` expect `example.txt` to exist.
- `filesystemshellmethods.py` can create/modify files such as:
  - `example.txt.bak`
  - `example_renamed.txt`
  - `archive.zip`
  - `testzip.zip`
- `challege-solution.py` expects a `deps` directory containing `.txt` files.

## Quick setup (if needed)

Create `example.txt`:

```powershell
Set-Content .\example.txt "First line`nSecond line"
```

Create sample files for challenge script:

```powershell
New-Item -ItemType Directory -Force .\deps
Set-Content .\deps\a.txt "hello"
Set-Content .\deps\b.txt "world"
```

## How to run

```powershell
python .\filehandling1.py
python .\filehandling2.py
python .\pathutils.py
python .\pathutils-pathlib.py
python .\filesystemshellmethods.py
python .\challege-solution.py
```

## Suggested order

1. `pathutils.py`
2. `pathutils-pathlib.py`
3. `filehandling1.py`
4. `filehandling2.py`
5. `filesystemshellmethods.py`
6. `challege-solution.py`
