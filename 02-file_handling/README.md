# Chapter 2: File Handling

This chapter covers foundational file and path operations in Python.

## Prerequisites

- Python 3.x
- Run scripts from inside this folder:

```powershell
cd 02-file_handling
```

## Files and topics

| File | Focus |
| --- | --- |
| `filehandling1.py` | Reading files with `readline()`, `readlines()`, `seek()` |
| `filehandling2.py` | Writing lines to a file, then reading and printing them |
| `pathutils.py` | `os` and `os.path` utilities: existence checks, metadata, timestamps |
| `pathutils-pathlib.py` | `pathlib.Path` version of common path/file operations |
| `filesystem-shell-methods.py` | Copy, rename, and archive files (`shutil`, `zipfile`) |
| `challenge-solution.py` | Challenge: total byte size of `.txt` files in `deps/` |

## Important notes

- `filehandling1.py` expects `example.txt` to exist.
- `filesystem-shell-methods.py` creates files such as `example.txt.bak`, `example_renamed.txt`, `archive.zip`, and `testzip.zip`.
- `challenge-solution.py` auto-creates `deps/` with sample `.txt` files if missing.

## Quick setup (if needed)

Create `example.txt`:

```powershell
Set-Content .\example.txt "First line`nSecond line"
```

## How to run

```powershell
python .\filehandling1.py
python .\filehandling2.py
python .\pathutils.py
python .\pathutils-pathlib.py
python .\filesystem-shell-methods.py
python .\challenge-solution.py
```

## Suggested order

1. `pathutils.py`
2. `pathutils-pathlib.py`
3. `filehandling1.py`
4. `filehandling2.py`
5. `filesystem-shell-methods.py`
6. `challenge-solution.py`
