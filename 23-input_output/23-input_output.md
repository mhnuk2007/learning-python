# Chapter 23 – Input/Output

## Learning Goals

- Master file reading and writing operations.
- Use context managers for safe resource handling.
- Handle errors during file operations.
- Process data from input to output files.

## Core Concepts

### Opening Files

```python
# Basic open
f = open('file.txt', 'r')
f.close()

# With context manager (recommended)
with open('file.txt', 'r') as f:
    data = f.read()
```

### File Modes

| Mode | Description |
| --- | --- |
| `'r'` | Read (default) |
| `'w'` | Write (overwrites) |
| `'a'` | Append |
| `'x'` | Create (fails if exists) |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |

### Reading Patterns

```python
# Read all
content = f.read()

# Read line by line
for line in f:
    print(line.strip())

# Read into list
lines = f.readlines()
```

### Writing Patterns

```python
# Write string
f.write("Hello\n")

# Print to file
print("Hello", file=f)
```

## Best Practices

- Always use `with` for automatic cleanup
- Strip whitespace when reading lines
- Handle exceptions for robust code
- Use try/except for type conversion
- Process input and generate output in one pass

## Common Mistakes

- Forgetting to close files
- Not handling file not found errors
- Ignoring empty lines when processing