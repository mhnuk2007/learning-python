# Chapter 13: Loops

Iteration patterns with `for` and `while` loops in Python.

## Status

- In Progress

## Prerequisites

- Python 3.x
- Understanding of variables and data types (Chapter 01)
- Understanding of conditionals (Chapter 12)

## How to run

```powershell
cd 13-loops
python .\for-loops.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `for-loops.py` | Iterating over sequences with `for` |
| `while-loops.py` | Conditional iteration with `while` |
| `loop-control.py` | `break`, `continue`, and `else` clauses |
| `enumerate-zip.py` | Using `enumerate()` and `zip()` for elegant iteration |
| `nested-loops.py` | Loops inside loops |

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
```

### Loop Control

```python
for item in items:
    if skip_condition:
        continue  # skip to next iteration
    if stop_condition:
        break     # exit loop entirely
else:
    # executed if loop completed without break
```

### Enumerate and Zip

```python
for index, value in enumerate(items):
    print(f"{index}: {value}")

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Notes

- Loops were previously covered in `01-fundamentals/loops.py`
- This chapter provides deeper coverage of iteration patterns

## Theory Notes

- [`13-loops.md`](13-loops.md)