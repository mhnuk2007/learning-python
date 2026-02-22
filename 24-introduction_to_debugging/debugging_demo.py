"""
========================================
PYTHON ERRORS & DEBUGGING – PRACTICE MODULE
========================================

This program demonstrates:

1. Syntax Errors (commented out for safe execution)
2. Runtime Errors (handled safely)
3. Logic Errors
4. Debugging techniques (print, try/except, pdb)
"""

import pdb

print("=== PYTHON ERRORS & DEBUGGING DEMO ===\n")

# =========================================
# 1️⃣ Syntax Error Example (Commented Out)
# =========================================
# Uncomment to see SyntaxError
# print("Hello World"    # <- Missing closing parenthesis
# for i in range(3)      # <- Missing colon
#     print(i)

print("Syntax error examples are commented out for safe execution.\n")

# =========================================
# 2️⃣ Runtime Error Examples
# =========================================

print("Runtime error demonstration:")

# Division by zero
x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError as e:
    print("Caught a runtime error:", e)

# Invalid type conversion
user_input = "abc"
try:
    number = int(user_input)
except ValueError as e:
    print("Caught a runtime error:", e)

# File not found
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("Caught a runtime error:", e)

print("\nRuntime errors handled safely.\n")

# =========================================
# 3️⃣ Logic Error Example
# =========================================

print("Logic error demonstration:")

numbers = [10, 20, 30]

# Bug: Using wrong formula
average_bug = sum(numbers) / (len(numbers) - 1)  # Logic error
print("Incorrect average (logic error):", average_bug)

# Correct calculation
average_correct = sum(numbers) / len(numbers)
print("Correct average:", average_correct)

# Another logic error with conditional
age = -5
if age > 0:
    print("Age is valid:", age)
else:
    print("Age is invalid (logic error check)")

print("\nLogic errors require reasoning and testing.\n")

# =========================================
# 4️⃣ Debugging Techniques
# =========================================

print("Debugging demonstration:")

# Example 1: Print debugging
total = 0
for i in range(5):
    print("Current i:", i)  # Inspect variable
    total += i
print("Total sum:", total)

# Example 2: Using pdb debugger
print("\nUsing pdb to inspect variables:")
a = 5
b = 0

# Uncomment the next line to interact with debugger
# pdb.set_trace()
# result_debug = a / b  # Will cause ZeroDivisionError in pdb

# Example 3: Defensive coding with try/except
try:
    result_safe = a / b
except ZeroDivisionError:
    print("Handled ZeroDivisionError safely in debugging example.")

print("\n=== End of Demo ===")