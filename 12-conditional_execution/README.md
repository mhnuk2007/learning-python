# Chapter 12: Conditional Execution

Control flow with conditional statements and decision-making in Python.

## Status

- In Progress

## Prerequisites

- Python 3.10+ (for `match/case` statements)
- Understanding of variables and data types (Chapter 01)

## How to run

```powershell
cd 12-conditional_execution
python .\conditionals.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `conditionals.py` | `if/elif/else` statements and comparison operators |
| `ternary.py` | Ternary conditional expressions |
| `match-case.py` | Pattern matching with `match/case` (Python 3.10+) |
| `logical-operators.py` | `and`, `or`, `not` for compound conditions |

## Key concepts

### Basic Conditionals

```python
if condition:
    # executed if condition is True
elif another_condition:
    # executed if another_condition is True
else:
    # executed if no conditions match
```

### Ternary Expression

```python
result = value_if_true if condition else value_if_false
```

### Pattern Matching (Python 3.10+)

```python
match value:
    case pattern1:
        # handle pattern1
    case pattern2:
        # handle pattern2
    case _:
        # default case
```

## Notes

- Conditionals were previously covered in `01-fundamentals/conditionals.py`
- This chapter provides deeper coverage of conditional patterns

## Theory Notes

- [`12-conditional_execution.md`](12-conditional_execution.md)