# Chapter 21: Iteration

Iteration techniques for Python collections.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of collections (Chapter 20)
- Understanding of loops (Chapter 13)

## How to run

```powershell
cd 21-iteration
python .\list-iteration.py
python .\dictionary-iteration.py
python .\tuple-iteration.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `list-iteration.py` | for/while loops, enumerate, reverse, safe modification, comprehension |
| `dictionary-iteration.py` | keys/values/items, enumerate, safe deletion, sorting, comprehension |
| `tuple-iteration.py` | basic iteration, unpacking, nested tuples, generator expressions |
| `chapter-challenge.py` | Practice exercises |

## Key concepts

### List Iteration

```python
for city in capitals:
    print(city)

for index, city in enumerate(capitals):
    print(f"{index}: {city}")

for city in reversed(capitals):
    print(city)
```

### Dictionary Iteration

```python
for key in dict:              # keys
for value in dict.values():   # values
for k, v in dict.items():     # key-value pairs
```

### Tuple Iteration

```python
for item in my_tuple:
    print(item)

# Unpacking
for name, role, salary in employees:
    print(f"{name}: {role}")
```

### Safe Modification

```python
# List: iterate over copy
for item in my_list[:]:
    if condition:
        my_list.remove(item)

# Dictionary: iterate over list of keys
for key in list(dict.keys()):
    if condition:
        del dict[key]
```

## Time Complexity

| Operation | List | Dict | Tuple |
| --- | --- | --- | --- |
| Iteration | O(n) | O(n) | O(n) |
| Membership | O(n) | O(1) | O(n) |

## Notes

- Use `enumerate()` for index-value pairs
- Never modify collection while iterating directly
- Dictionary membership is O(1) due to hashing
- Use generator expressions for memory efficiency

## Theory Notes

- [`21-iteration.md`](21-iteration.md)