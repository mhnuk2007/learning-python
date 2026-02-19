# Chapter 11: Sets and Dictionaries

Hash-based collections for unique elements and key-value lookups.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of lists and tuples (Chapter 09)

## How to run

```powershell
cd 11-sets_and_dictionaries
python .\sets.py
```

Replace `sets.py` with any file in this chapter.

## Files and topics

### Sets

| File | Focus |
| --- | --- |
| `sets.py` | Set creation, union, intersection, difference, symmetric difference |
| `sets2.py` | Set operations with hobbies example |
| `sort-in-sets.py` | Combining set operations: intersection → difference → symmetric difference |
| `add-remove-in-sets.py` | `add()`, `remove()`, `pop()`, and membership testing |

### Dictionaries

| File | Focus |
| --- | --- |
| `dictionaries.py` | Dictionary basics: access, add, update, remove, iterate |
| `add-to-dictionary.py` | Adding entries, updating values, storing multiple values |
| `nested-dictionary.py` | Nested dictionaries for structured data (contact manager) |
| `reverse-lookup-in-dictionary.py` | Finding keys by value (reverse lookup) |

### Combined

| File | Focus |
| --- | --- |
| `sets_and_dictionaries.py` | Quick demo of both sets and dictionaries with comprehensions |

## Key concepts

### Sets

Sets are unordered collections of unique elements.

```python
# Creation
friends = {'Alice', 'Bob', 'Carol'}
numbers = set([1, 2, 2, 3])  # {1, 2, 3}

# Operations
a.union(b)           # a | b
a.intersection(b)    # a & b
a.difference(b)      # a - b
a.symmetric_difference(b)  # a ^ b

# Modification
friends.add('Dave')
friends.remove('Alice')  # Raises KeyError if not found
friends.pop()            # Remove arbitrary element
```

### Dictionaries

Dictionaries are key-value pairs with fast lookup.

```python
# Creation
rolodex = {'Alice': 5551234, 'Bob': 5555678}

# Access
rolodex['Alice']           # 5551234
rolodex.get('Dave', None)  # None (safe access)

# Modification
rolodex['Carol'] = 5559999  # Add
rolodex['Alice'] = 5550000  # Update
rolodex.pop('Bob')          # Remove

# Iteration
for name, number in rolodex.items():
    print(f"{name}: {number}")
```

### Nested Dictionaries

```python
contacts = {
    'Alice': {'phone': 5551234, 'email': 'alice@example.com'},
    'Bob': {'phone': 5555678, 'email': 'bob@example.com'}
}

# Access nested value
contacts['Alice']['email']
```

## Notes

- Sets are unordered and contain only unique elements
- Dictionaries keys must be hashable (immutable types)
- `set.pop()` removes an arbitrary element (sets are unordered)
- `dict.pop(key)` removes a specific key
- Reverse lookup requires iterating through items

## Theory Notes

- [`11-sets_and_dictionaries.md`](11-sets_and_dictionaries.md)