# Chapter 15: Comprehensions

Concise collection construction patterns.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of loops (Chapter 13)
- Understanding of lists, sets, and dictionaries (Chapter 09, 11)

## How to run

```powershell
cd 15-comprehensions
python .\list-comprehensions.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `list-comprehensions.py` | List comprehensions: `[x for x in iterable]` |
| `set-comprehensions.py` | Set comprehensions: `{x for x in iterable}` |
| `dict-comprehensions.py` | Dict comprehensions: `{k: v for k, v in iterable}` |
| `generator-expressions.py` | Generator expressions: `(x for x in iterable)` |
| `nested-comprehensions.py` | Nested comprehensions for multi-dimensional data |
| `comprehension-pitfalls.py` | Common pitfalls and readability tips |
| `comprehension-recap.py` | Quick recap with list, dict, and set examples |
| `comprehensions.py` | Original comprehensive examples |

## Key concepts

### List Comprehension

```python
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Set Comprehension

```python
unique_lengths = {len(word) for word in words}
```

### Dict Comprehension

```python
word_lengths = {word: len(word) for word in words}
```

### Generator Expression

```python
square_gen = (x**2 for x in range(10))  # lazy evaluation
sum_squares = sum(x**2 for x in range(10))
```

### Nested Comprehension

```python
flat = [num for row in matrix for num in row]
```

## Notes

- Comprehensions are concise but should remain readable
- Use `if` clauses for filtering
- Generators are memory-efficient for large sequences
- Prefer explicit loops when logic becomes complex

## Theory Notes

- [`15-comprehensions.md`](15-comprehensions.md)