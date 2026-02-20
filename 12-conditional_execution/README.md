# Chapter 12: Conditional Execution

Control flow with conditional statements and decision-making in Python.

## Status

- Completed

## Prerequisites

- Python 3.10+ (for `match/case` statements)
- Understanding of variables and data types (Chapter 01)

## How to run

```powershell
cd 12-conditional_execution
python .\conditionals.py
```

## Files and topics

### Basic Conditionals

| File | Focus |
| --- | --- |
| `if-condition.py` | Basic `if` statement with a single condition |
| `if-else-condition.py` | `if/else` for two-way decisions |
| `if-elif-condition.py` | `if/elif/else` for multiple branches (grade example) |
| `if-elif-condition2.py` | Multiple conditions with logical operators (pizza ordering) |
| `conditionals.py` | Collection of conditional functions (positive/negative, grades, comparison) |

### Ternary Expressions

| File | Focus |
| --- | --- |
| `ternary.py` | One-line conditional expressions: `value if condition else other` |

### Pattern Matching

| File | Focus |
| --- | --- |
| `match-case.py` | `match/case` statement for structural pattern matching (day specials) |
| `match-case2.py` | OR patterns in `match/case` (`|` operator for multiple matches) |

### Advanced Techniques

| File | Focus |
| --- | --- |
| `logical-operators.py` | `and`, `or`, `not` operators for compound conditions |
| `condition-using-set.py` | Using sets and `issubset()` in conditions |

## Key concepts

### Basic Conditionals

```python
if condition:
    # executed if True
elif another_condition:
    # executed if first is False and this is True
else:
    # executed if all conditions are False
```

### Ternary Expression

```python
status = "Adult" if age >= 18 else "Minor"
maximum = a if a > b else b
```

### Pattern Matching (Python 3.10+)

```python
match day:
    case 'Saturday' | 'Sunday':
        print("Weekend!")
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print("Weekday")
    case _:
        print("Invalid day")
```

### Logical Operators

```python
if age >= 18 and has_id:      # Both must be True
if is_raining or is_cold:     # At least one must be True
if not username:              # Negation
if 10 < number < 20:          # Chained comparison
```

### Set-based Conditions

```python
if {'meat', 'cheese'}.issubset(diet_restrictions):
    print("Get a vegan pizza")
```

## Notes

- Pattern matching (`match/case`) requires Python 3.10+
- The `_` case is the default (wildcard) pattern in `match`
- Ternary expressions are best for simple, readable one-liners
- Use logical operators to combine multiple conditions

## Theory Notes

- [`12-conditional_execution.md`](12-conditional_execution.md)