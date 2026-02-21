# Chapter 20: Collections

Python's core collection types: Lists, Dictionaries, and Tuples.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of variables and basic types

## How to run

```powershell
cd 20-collections
python .\list.py
python .\dictionary.py
python .\tuple.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `list.py` | Lists: creation, indexing, slicing, mutability, methods, shallow/deep copy |
| `dictionary.py` | Dictionaries: key-value pairs, methods, nested dicts, copy behavior |
| `tuple.py` | Tuples: immutability, unpacking, named tuples |
| `chapter_challenge.py` | Practice: stars list and peaks dictionary |

## Key concepts

### Lists

```python
capitals = ["Karachi", "Lahore", "Peshawar"]
capitals[0] = "Islamabad"  # mutable
capitals.append("Quetta")
capitals.sort()
```

### Dictionaries

```python
symbols = {'bird': 'Chukar', 'animal': 'Markhor'}
symbols['flower'] = 'Jasmine'  # add/update
symbols.get('sport', 'Not Defined')  # safe access
```

### Tuples

```python
info = ("Islamabad", 240, "PKR")  # immutable
capital, pop, currency = info  # unpacking
```

### Shallow vs Deep Copy

```python
import copy
shallow = original.copy()      # outer copy only
deep = copy.deepcopy(original)  # full independent copy
```

## Comparison

| Type | Mutable | Ordered | Use Case |
| --- | --- | --- | --- |
| List | Yes | Yes | Dynamic sequences |
| Dictionary | Yes | Yes (3.7+) | Key-value mappings |
| Tuple | No | Yes | Fixed, read-only data |

## Notes

- Lists are mutable; tuples are immutable
- Dictionary membership testing is O(1)
- Use `namedtuple` for readable tuple access
- Deep copy for fully independent nested structures

## Theory Notes

- [`20-collections.md`](20-collections.md)