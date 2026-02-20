# Chapter 18: Misc Tools

Useful standard library utilities used in day-to-day scripts.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of functions (Chapter 04)
- Understanding of loops (Chapter 13)

## How to run

```powershell
cd 18-misc_tools
python .\random-utilities.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `random-utilities.py` | `random.randint()`, `choice()`, `shuffle()`, `sample()`, `seed()` |
| `itertools-utilities.py` | `product()`, `permutations()`, `combinations()`, `count()`, `cycle()`, `repeat()` |
| `functools-utilities.py` | `reduce()`, `lru_cache` for memoization |
| `combining-tools.py` | Combining random and itertools together |
| `misc-tools-demo.py` | Original comprehensive examples |

## Key concepts

### Random Module

```python
import random
random.randint(1, 10)      # Random integer 1-10
random.choice(['a', 'b'])  # Random element
random.shuffle(list)       # Shuffle in place
random.sample(list, 3)     # Sample without replacement
random.seed(42)            # Set seed for reproducibility
```

### Itertools Module

```python
import itertools
itertools.product(a, b)       # Cartesian product
itertools.permutations(items) # All permutations
itertools.combinations(items, 2)  # Combinations of size 2
itertools.count(start, step)  # Infinite counter
itertools.cycle(items)        # Infinite cycle
itertools.repeat(item, n)     # Repeat n times
```

### Functools Module

```python
from functools import reduce, lru_cache
reduce(lambda x, y: x + y, nums)  # Reduce to single value

@lru_cache(maxsize=None)
def fib(n):  # Memoized function
    ...
```

## Notes

- Use `random.seed()` for reproducible random results
- `itertools` provides memory-efficient iterators
- `lru_cache` is great for expensive function calls
- Combine modules for powerful utilities

## Theory Notes

- [`18-misc_tools.md`](18-misc_tools.md)