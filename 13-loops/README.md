# Chapter 13: Loops

Iteration patterns with `for` and `while` loops in Python.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of variables and data types (Chapter 01)
- Understanding of conditionals (Chapter 12)

## How to run

```powershell
cd 13-loops
python .\loops.py
```

## Files and topics

### For Loops

| File | Focus |
| --- | --- |
| `for-loop.py` | Basic `for` loop iteration (dishwasher example) |
| `loops.py` | Simple `for` and `while` loop examples with `range()` |
| `for-break.py` | Using `break` to exit a `for` loop early |

### While Loops

| File | Focus |
| --- | --- |
| `while-loop.py` | Basic `while` loop with list (dishwasher example) |
| `while-loop2.py` | `while True` with `break` (scrubbing pan example) |
| `while-loop3.py` | `while` with compound condition (cabinet capacity example) |

### Loop Control

| File | Focus |
| --- | --- |
| `loop-control.py` | `break`, `continue`, and `pass` statements |
| `loop-else.py` | `else` clause that runs when loop completes without `break` |

### Iterating Collections

| File | Focus |
| --- | --- |
| `loop-collections.py` | Looping over lists, sets, and dictionaries |
| `enumerate-and-zip.py` | Using `enumerate()` for index/value and `zip()` for parallel iteration |

## Key concepts

### For Loop

```python
for item in iterable:
    # process item

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### While Loop

```python
while condition:
    # executed while condition is True

while True:
    # infinite loop until break
    if done:
        break
```

### Loop Control

```python
for item in items:
    if skip_condition:
        continue  # skip to next iteration
    if stop_condition:
        break     # exit loop entirely
    pass          # placeholder, does nothing
```

### Loop Else Clause

```python
for item in items:
    if item == target:
        print("Found!")
        break
else:
    print("Not found!")  # runs if loop completed without break
```

### Enumerate and Zip

```python
# Get index and value
for index, value in enumerate(items):
    print(f"{index}: {value}")

# Iterate multiple sequences in parallel
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Notes

- `for` loops are ideal for known sequences
- `while` loops are ideal for unknown iteration counts
- `break` exits the loop; `continue` skips to next iteration
- `else` clause executes only if loop completes without `break`
- Use `enumerate()` for index/value pairs; use `zip()` for parallel iteration

## Theory Notes

- [`13-loops.md`](13-loops.md)