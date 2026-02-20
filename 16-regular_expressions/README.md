# Chapter 16: Regular Expressions

Text pattern matching with Python's `re` module.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of strings (Chapter 01)

## How to run

```powershell
cd 16-regular_expressions
python .\simple-search.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `simple-search.py` | `re.search()` - find first match |
| `find-all-matches.py` | `re.findall()` - find all matches |
| `regex-substitution.py` | `re.sub()` - replace patterns |
| `capture-groups.py` | Extract parts with `()` groups |
| `raw-strings.py` | Using `r"..."` for patterns |
| `character-classes.py` | Character sets `[a-zA-Z0-9]` |
| `quantifiers.py` | `{n}`, `{n,m}`, `*`, `+`, `?` |
| `optional-alternation.py` | Optional `?` and alternation `\|` |
| `anchors.py` | Start `^` and end `$` anchors |
| `regex-split.py` | `re.split()` - split by pattern |
| `regex-pitfalls.py` | Common mistakes and best practices |
| `regex-basics.py` | Original comprehensive examples |

## Key concepts

### Basic Functions

```python
re.search(pattern, text)   # Find first match
re.findall(pattern, text)  # Find all matches
re.sub(pattern, repl, text)  # Replace matches
re.split(pattern, text)    # Split by pattern
```

### Common Patterns

```python
\d      # Digit (0-9)
\w      # Word character (a-z, A-Z, 0-9, _)
.       # Any character
\s      # Whitespace
```

### Quantifiers

```python
*       # Zero or more
+       # One or more
?       # Zero or one (optional)
{n}     # Exactly n
{n,m}   # Between n and m
```

### Character Classes

```python
[abc]       # a, b, or c
[a-z]       # Any lowercase letter
[^abc]      # Not a, b, or c
```

## Notes

- Use raw strings `r"pattern"` to avoid escape issues
- Escape special characters with `\` (`.`, `*`, `?`, etc.)
- Prefer string methods for simple operations (`startswith`, `in`)
- Regex is powerful but can be overkill for simple tasks

## Theory Notes

- [`16-regular_expressions.md`](16-regular_expressions.md)