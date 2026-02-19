# Chapter 4: Functions

This chapter focuses on Python functions - defining them, passing parameters, using global variables, and code reuse patterns.

## Prerequisites

- Python 3.x
- Terminal access (PowerShell, CMD, or Bash)

## How to run

From the project root:

```powershell
cd chapter4-Functions
python .\basic-function.py
```

Replace `basic-function.py` with any file in this chapter.

## Files and topics

| File | Focus |
| --- | --- |
| `basic-function.py` | Function definition, calling functions, return values |
| `function-code-reuse.py` | Functions calling other functions, code reuse patterns |
| `function-with-parameters.py` | Single parameter functions, passing arguments |
| `multi-parameters-functions.py` | Multiple parameters, `*args` for variable arguments |
| `global-scope-variable.py` | Global variables, `global` keyword, variable scope |

## Suggested order

1. `basic-function.py`
2. `function-code-reuse.py`
3. `function-with-parameters.py`
4. `multi-parameters-functions.py`
5. `global-scope-variable.py`

## Key concepts

### Defining functions

```python
def make_pancakes():
    print("Mixing ingredients")
    return "a stack of fluffy pancakes"

# Call the function
breakfast = make_pancakes()
```

### Parameters and arguments

```python
# Single parameter
def make_pizza(topping):
    return f"a {topping} pizza"

# Multiple parameters
def make_burger(cheese, sauce):
    return f"a burger with {cheese} and {sauce}"

# Variable arguments (*args)
def make_deluxe_burger(*toppings):
    return f"a burger with {len(toppings)} toppings"
```

### Global variables

```python
sauce = 'tomato'  # Global variable

def make_pizza():
    # Reads global variable
    return f"a pizza with {sauce} sauce"

def make_special_pizza():
    global sauce  # Required to modify global
    sauce = 'pesto'
    return f"a special pizza with {sauce} sauce"
```

## Notes

- All examples use food-related metaphors to make concepts memorable
- Files are independent and can be run in any order, but following the suggested order is recommended
- `global-scope-variable.py` demonstrates how the `global` keyword affects variable modification