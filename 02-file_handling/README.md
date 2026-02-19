# Chapter 02: File Handling

Core file and path operations in Python.

## Status

- Completed

## Prerequisites

- Python 3.x

## How to run

```powershell
cd 02-file_handling
python .\filehandling1.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `filehandling1.py` | Read files with `readline()`, `readlines()`, `seek()` |
| `filehandling2.py` | Write text and read it back |
| `pathutils.py` | `os` and `os.path` utilities |
| `pathutils-pathlib.py` | `pathlib.Path` alternatives |
| `filesystem-shell-methods.py` | Copy, rename, and archive files |
| `challenge-solution.py` | Total byte size of `.txt` files in `deps/` |

## Notes

- `filesystem-shell-methods.py` generates `example.txt.bak`, `example_renamed.txt`, `archive.zip`, and `testzip.zip`.
- `challenge-solution.py` creates sample files in `deps/` if needed.
