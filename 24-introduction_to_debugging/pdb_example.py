"""
========================================
PYTHON DEBUGGER (pdb) – DEMONSTRATION
========================================

This program demonstrates using pdb for debugging.

pdb Commands:
n (next)    - Execute next line
c (continue) - Continue execution
p var       - Print variable value
l (list)    - Show current code
q (quit)    - Quit debugger
"""

import pdb

print("=== PDB DEBUGGER DEMO ===\n")

# =========================================
# Example 1: Basic pdb usage
# =========================================

print("Example 1: Basic debugging")
print("Uncomment pdb.set_trace() to start debugger\n")

x = 10
y = 0

# Uncomment the next line to start debugger
# pdb.set_trace()

# result = x / y  # This would crash

# =========================================
# Example 2: Debugging a function
# =========================================

def calculate_average(numbers):
    """Calculate average of a list."""
    if not numbers:
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    
    # Uncomment to debug
    # pdb.set_trace()
    
    return total / count

print("Example 2: Debugging a function")
values = [10, 20, 30, 40, 50]
avg = calculate_average(values)
print(f"Average: {avg}\n")

# =========================================
# Example 3: Debugging a loop
# =========================================

print("Example 3: Debugging a loop")

total = 0
for i in range(5):
    # Uncomment to debug each iteration
    # pdb.set_trace()
    
    total += i
    print(f"  i={i}, total={total}")

print(f"Final total: {total}\n")

# =========================================
# Example 4: Using breakpoint() (Python 3.7+)
# =========================================

print("Example 4: Using breakpoint()")
print("breakpoint() is the modern way to start debugger")
print("Uncomment to try\n")

# a = 5
# b = 10
# breakpoint()
# c = a + b

# =========================================
# Summary
# =========================================

print("=== PDB COMMANDS SUMMARY ===")
print("""
Command  | Action
---------|------------------
n        | Next line
s        | Step into function
c        | Continue execution
p var    | Print variable
pp var   | Pretty print
l        | List source code
w        | Show call stack
q        | Quit debugger
help     | Show help
""")