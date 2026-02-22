# Chapter 24 – Introduction to Debugging

## Learning Goals

- Understand what debugging is and why it matters.
- Identify the three types of errors: syntax, runtime, logic.
- Learn to read and interpret error messages.
- Master debugging techniques: print, pdb, IDE debuggers.
- Apply defensive coding to prevent bugs.

## Types of Errors

### Syntax Errors

Code violates Python grammar rules. Program won't run.

```python
# Missing parenthesis
print("Hello"
# SyntaxError: '(' was never closed
```

### Runtime Errors

Occur during execution. Can be handled.

```python
x = 10 / 0  # ZeroDivisionError
int("abc")  # ValueError
items[10]   # IndexError (if list is shorter)
```

### Logic Errors

Program runs but produces wrong results.

```python
# Bug: wrong formula
average = sum(numbers) / (len(numbers) - 1)
```

## Debugging Techniques

### Print Debugging

```python
for i in range(5):
    print(f"i = {i}")  # Inspect values
```

### Using pdb

```python
import pdb
pdb.set_trace()  # Pause execution

# Commands: n (next), c (continue), p var (print), q (quit)
```

### IDE Debuggers

- Set breakpoints
- Step over/into functions
- Inspect variables
- Watch expressions

## Defensive Coding

1. Validate input
2. Check before operations
3. Use assertions
4. Handle exceptions
5. Return early for invalid cases

## Best Practices

- Read error messages carefully
- Reproduce the bug first
- Simplify code to isolate problem
- Test with edge cases
- Make one change at a time