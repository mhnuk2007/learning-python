# Chapter 22 – Strings

## Learning Goals

- Master string creation, indexing, and slicing.
- Learn string methods for manipulation.
- Understand pattern searching and regex.
- Apply formatting and cleaning techniques.

## Core Concepts

### String Basics

```python
name = "Honey Chauhan"
name[0]        # 'H' (indexing)
name[-1]       # 'n' (negative index)
name[:5]       # 'Honey' (slicing)
name[::-1]     # reversed
```

### String Methods

```python
text.upper()           # uppercase
text.lower()           # lowercase
text.strip()           # remove whitespace
text.replace("a", "b") # replace
text.split()           # split to list
"-".join(list)         # join to string
text.find("pattern")   # first index
text.count("pattern")  # occurrences
```

### Formatting

```python
# f-string (recommended)
f"My name is {name} and I am {age}"

# format() method
"My name is {}".format(name)
```

### Pattern Searching

```python
# Basic
"Python" in text
text.startswith("Py")
text.endswith(".py")

# Regex
import re
re.findall(r"\d+", text)    # find all numbers
re.sub(r"\d+", "X", text)   # replace
re.match(r"^\w+$", text)    # validate
```

## Best Practices

- Strings are immutable - create new strings for changes
- Use `join()` for efficient concatenation in loops
- Use `strip()` to clean user input
- Use f-strings for readable formatting
- Use regex for complex pattern matching

## Common Mistakes

- Modifying strings in loops inefficiently
- Forgetting strings are immutable
- Not normalizing case for comparisons