# 13-loops

## Learning goals

- Master `for` loops for iterating over sequences.
- Use `while` loops for conditional iteration.
- Control loop flow with `break`, `continue`, and `else`.
- Apply `enumerate()` and `zip()` for elegant iteration.

## Key definitions

- `Iteration`: repeating a block of code for each item in a sequence.
- `Iterable`: an object that can be looped over (list, tuple, string, etc.).
- `Iterator`: an object that produces the next value on each `next()` call.

## Core concepts

### For Loop

The `for` loop iterates over any iterable:

```python
for item in [1, 2, 3]:
    print(item)
```

### While Loop

The `while` loop runs as long as a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Range Function

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

### Loop Else Clause

The `else` block runs if the loop completes without `break`:

```python
for item in items:
    if found:
        break
else:
    print("Not found")
```

## Common mistakes

- Off-by-one errors with `range()`.
- Infinite `while` loops (forgetting to update the condition).
- Modifying a list while iterating over it.
- Using `for` when `while` is more appropriate (or vice versa).

## Quick recap

- `for` loops are ideal for known sequences.
- `while` loops are ideal for unknown iteration counts.
- `break` exits the loop; `continue` skips to next iteration.
- `enumerate()` provides index and value; `zip()` pairs items.