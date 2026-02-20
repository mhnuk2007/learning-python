# Chapter 14: Error Handling

Exception handling patterns, including custom exceptions and practical examples.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of conditionals (Chapter 12)

## How to run

```powershell
cd 14-error_handling
python .\error-handling.py
```

## Files and topics

### Basic Exception Handling

| File | Focus |
| --- | --- |
| `error-handling.py` | `try/except/else/finally` flow with division example |
| `specific-exceptions.py` | Catching specific exceptions: `IndexError`, `TypeError` |
| `file-errors.py` | Handling file-related errors: `FileNotFoundError`, `PermissionError` |
| `multiple-exceptions.py` | Handling multiple exception types in one block |

### Raising and Creating Exceptions

| File | Focus |
| --- | --- |
| `raising-exceptions.py` | Using `raise` to trigger exceptions manually |
| `custom-exception.py` | Creating custom exception classes (`InvalidAgeError`) |
| `custom-errors.py` | Extended custom exception examples |
| `household-errors.py` | Custom exceptions with `__str__` override (`ElectricalError`, `PlumbingError`) |

### Assertions and Validation

| File | Focus |
| --- | --- |
| `assertions.py` | Using `assert` for debugging and validation |
| `validation-exceptions.py` | Raising exceptions for input validation |

### Practical Examples

| File | Focus |
| --- | --- |
| `url-errors.py` | Handling URL/download errors with `urllib.error.URLError` |
| `circuit-breaker.py` | Real-world class with exception handling (circuit breaker overload) |
| `exception-handling.py` | Interactive exception handling demo |

## Key concepts

### Try/Except/Else/Finally

```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Invalid type")
else:
    print("Result:", result)  # runs if no exception
finally:
    print("Done")  # always runs
```

### Raising Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

### Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

### Assertions

```python
def calculate_square_root(number):
    assert number >= 0, "Number must be non-negative"
    return number ** 0.5
```

## Notes

- Catch specific exceptions rather than using bare `except:`
- Use `else` clause for code that should run only when no exception occurs
- Use `finally` for cleanup code (closing files, releasing resources)
- Custom exceptions should inherit from `Exception` class
- Assertions are for debugging; use exceptions for runtime validation

## Theory Notes

- [`14-error_handling.md`](14-error_handling.md)