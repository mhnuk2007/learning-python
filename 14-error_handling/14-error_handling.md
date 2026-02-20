# 14-error_handling

## Learning goals

- Handle runtime errors safely.
- Design clear custom exception classes.
- Keep failure behavior explicit and predictable.

## Key definitions

- `Exception`: runtime error object.
- `try/except`: capture and handle errors.
- `finally`: block that always runs.
- `raise`: explicitly trigger an exception.

## Core concepts

- Catch specific exception types whenever possible.
- Use `else` for logic that should run only when no exception occurs.
- Use custom exceptions to model domain-specific errors.

## Common mistakes

- Broad `except Exception` used everywhere.
- Hiding errors without logging or context.

## Quick recap

- Good error handling improves reliability and debugging speed.