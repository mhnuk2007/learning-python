# Chapter 20 – Collections

## Learning Goals

- Understand Python's core collection types.
- Learn when to use lists, dictionaries, and tuples.
- Master shallow vs deep copy concepts.
- Apply comprehensions for transformations.

## Core Data Structures

### Lists

Ordered, mutable sequences.

```python
capitals = ["Karachi", "Lahore", "Peshawar"]
capitals[0] = "Islamabad"  # mutable
capitals.append("Quetta")
capitals.sort()
```

### Dictionaries

Key-value mappings, fast lookups.

```python
symbols = {'bird': 'Chukar', 'animal': 'Markhor'}
symbols.get('sport', 'Not Defined')  # safe access
```

### Tuples

Ordered, immutable sequences.

```python
info = ("Islamabad", 240, "PKR")
capital, pop, currency = info  # unpacking
```

## Advanced Concepts

### Shallow vs Deep Copy

```python
import copy
shallow = original.copy()       # outer copy only
deep = copy.deepcopy(original)  # full independent copy
```

### Named Tuples

```python
from collections import namedtuple
Country = namedtuple("Country", ["name", "capital"])
pakistan = Country("Pakistan", "Islamabad")
print(pakistan.capital)  # access by name
```

### Comprehensions

```python
squares = [x ** 2 for x in range(5)]
cubes = {x: x ** 3 for x in range(5)}
```

## Comparison Table

| Feature | List | Dictionary | Tuple |
| --- | --- | --- | --- |
| Mutable | Yes | Yes | No |
| Ordered | Yes | Yes (3.7+) | Yes |
| Indexed | Integer | Key | Integer |
| Membership | O(n) | O(1) | O(n) |

## Best Practices

- Use lists for dynamic sequences
- Use dictionaries for key-value lookups
- Use tuples for fixed, read-only data
- Use `get()` for safe dictionary access
- Use deep copy for fully independent nested structures