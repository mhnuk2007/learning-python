# Chapter 23: Input/Output

File input/output operations with proper resource management.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of file handling basics

## How to run

```powershell
cd 23-input_output
python .\io-process.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `io-process.py` | Reading, writing, context manager, error handling |
| `io-input-values.txt` | Input data file with numbers |
| `io-output-totaled.txt` | Generated output file with results |

## Key concepts

### Context Manager

```python
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed
```

### File Modes

| Mode | Description |
| --- | --- |
| `'r'` | Read (default) |
| `'w'` | Write (overwrites) |
| `'a'` | Append |
| `'t'` | Text mode (default) |
| `'b'` | Binary mode |

### Reading Patterns

```python
# Read entire file
content = f.read()

# Read line by line
for line in f:
    print(line.strip())
```

### Writing Patterns

```python
# Write string
f.write("Hello\n")

# Print to file
print("Hello", file=f)
```

## Notes

- Always use `with` for automatic resource cleanup
- Handle exceptions for robust file operations
- Strip whitespace when reading line by line
- Use `'rt'` for text, `'rb'` for binary

## Theory Notes

- [`23-input_output.md`](23-input_output.md)