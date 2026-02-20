# 12-conditional_execution

## Learning goals

- Master conditional logic with `if/elif/else` statements.
- Use ternary expressions for concise conditionals.
- Apply pattern matching with `match/case` (Python 3.10+).
- Combine conditions with logical operators.

## Key definitions

- `Condition`: an expression that evaluates to `True` or `False`.
- `Branch`: a block of code that executes when a condition is met.
- `Ternary`: a one-line conditional expression.
- `Pattern matching`: matching values against structural patterns.

## Core concepts

### Comparison Operators

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Logical Operators

- `and`: True if both operands are True
- `or`: True if at least one operand is True
- `not`: Inverts the boolean value

### Truthiness

In Python, the following values are "falsy":
- `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `set()`

All other values are "truthy".

## Common mistakes

- Using `=` (assignment) instead of `==` (comparison).
- Forgetting colons after `if`, `elif`, `else`.
- Incorrect indentation in code blocks.
- Overcomplicating conditions when early returns would be clearer.

## Quick recap

- Use `if/elif/else` for multi-way decisions.
- Ternary expressions: `x if condition else y`.
- Pattern matching provides elegant multi-case handling.
- Keep conditions simple and readable.