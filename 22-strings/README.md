# Chapter 22: Strings

String manipulation, pattern searching, and text processing.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of basic data types

## How to run

```powershell
cd 22-strings
python .\strings.py
python .\finding-pattern.py
python .\string-combination-manipulatlation.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `strings.py` | Creation, indexing, slicing, methods, formatting, immutability |
| `finding-pattern.py` | Search methods, regex with `re` module, validation |
| `string-combination-manipulatlation.py` | Concatenation, join, formatting, padding, cleaning |
| `chapter-challenge.py` | Practice exercises |

## Key concepts

### String Methods

```python
text.upper()      # uppercase
text.lower()      # lowercase
text.strip()      # remove whitespace
text.replace()    # replace substring
text.split()      # split into list
"-".join(list)    # join list into string
```

### Searching

```python
"Python" in text      # membership test
text.find("Python")   # first index
text.count("Python")  # occurrences
text.startswith("Py") # prefix check
```

### Formatting

```python
# f-string (recommended)
f"My name is {name}"

# format() method
"My name is {}".format(name)
```

### Regex

```python
import re
re.findall(pattern, text)  # find all matches
re.sub(pattern, repl, text) # replace
re.match(pattern, text)     # validate
```

## Notes

- Strings are immutable
- Use `join()` for efficient concatenation
- Use `strip()` to clean input
- Use f-strings for formatting

## Theory Notes

- [`22-strings.md`](22-strings.md)