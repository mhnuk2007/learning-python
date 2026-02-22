# Chapter 24: Introduction to Debugging

Debugging techniques, error types, and defensive coding practices.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of basic programming concepts

## How to run

```powershell
cd 24-introduction_to_debugging
python .\debugging_demo.py
python .\error_types.py
python .\pdb_example.py
python .\defensive_coding.py
```

## Files and topics

| File | Focus |
| --- | --- |
| `debugging_demo.py` | Complete debugging demonstration with all error types |
| `error_types.py` | Syntax, runtime, and logic errors with examples |
| `pdb_example.py` | Using Python's built-in debugger |
| `defensive_coding.py` | Best practices for preventing bugs |

## Key concepts

### Types of Errors

| Error Type | When | Example |
| --- | --- | --- |
| Syntax Error | Before execution | Missing parenthesis |
| Runtime Error | During execution | Division by zero |
| Logic Error | After execution | Wrong formula |

### Debugging Techniques

```python
# Print debugging
print("Variable value:", x)

# Using pdb
import pdb
pdb.set_trace()

# Using breakpoint (Python 3.7+)
breakpoint()
```

### pdb Commands

| Command | Action |
| --- | --- |
| `n` | Next line |
| `c` | Continue |
| `p var` | Print variable |
| `l` | List code |
| `q` | Quit |

### Defensive Coding

- Validate input
- Check before operations
- Use assertions
- Handle exceptions
- Return early for invalid cases

## Notes

- Read error messages carefully
- Always reproduce the bug first
- Simplify code to isolate problems
- Test with edge cases

## Theory Notes

- [`24-introduction_to_debugging.md`](24-introduction_to_debugging.md)