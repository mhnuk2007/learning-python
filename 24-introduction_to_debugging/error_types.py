"""
========================================
PYTHON ERROR TYPES – DEMONSTRATION
========================================

This program demonstrates the three types of errors:
1. Syntax Errors
2. Runtime Errors
3. Logic Errors
"""

print("=== ERROR TYPES DEMO ===\n")

# =========================================
# 1️⃣ Syntax Errors (Commented - won't run)
# =========================================

print("1. SYNTAX ERRORS:")
print("   - Violate Python grammar rules")
print("   - Program won't run at all")
print("   - Detected by interpreter before execution\n")

# Example 1: Missing parenthesis (uncomment to see error)
# print("Hello World"

# Example 2: Missing colon (uncomment to see error)
# for i in range(3)
#     print(i)

# Example 3: Wrong indentation (uncomment to see error)
# if True:
# print("Wrong indent")

print("   Syntax errors are commented out for safe execution.\n")

# =========================================
# 2️⃣ Runtime Errors
# =========================================

print("2. RUNTIME ERRORS:")
print("   - Occur during execution")
print("   - Code is syntactically correct")
print("   - Can be handled with try/except\n")

# ZeroDivisionError
print("   Example: ZeroDivisionError")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Caught: {e}\n")

# ValueError
print("   Example: ValueError")
try:
    number = int("abc")
except ValueError as e:
    print(f"   Caught: {e}\n")

# IndexError
print("   Example: IndexError")
try:
    items = [1, 2, 3]
    item = items[10]
except IndexError as e:
    print(f"   Caught: {e}\n")

# TypeError
print("   Example: TypeError")
try:
    result = "string" + 5
except TypeError as e:
    print(f"   Caught: {e}\n")

# FileNotFoundError
print("   Example: FileNotFoundError")
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"   Caught: {e}\n")

# =========================================
# 3️⃣ Logic Errors
# =========================================

print("3. LOGIC ERRORS:")
print("   - Program runs without crashing")
print("   - Produces incorrect results")
print("   - Hardest to detect\n")

# Example: Average calculation bug
print("   Example: Wrong average calculation")
numbers = [10, 20, 30]

# Bug: dividing by len-1 instead of len
wrong_average = sum(numbers) / (len(numbers) - 1)
print(f"   Wrong average: {wrong_average}")

correct_average = sum(numbers) / len(numbers)
print(f"   Correct average: {correct_average}\n")

# Example: Off-by-one error
print("   Example: Off-by-one error in loop")
total = 0
for i in range(5):  # 0, 1, 2, 3, 4 (not 5!)
    total += i
print(f"   Sum of 0-4: {total}")
print(f"   You might expect 15 (1+2+3+4+5) but got {total}\n")

# Example: Wrong condition
print("   Example: Wrong condition")
age = -5
if age > 0:  # Should check age >= 0 for valid ages
    print("   Valid age")
else:
    print("   Invalid age detected\n")

# =========================================
# Summary
# =========================================

print("=== SUMMARY ===")
print("""
| Error Type   | When            | Detectable By    |
|--------------|-----------------|------------------|
| Syntax Error | Before run      | Interpreter      |
| Runtime Err  | During run      | try/except       |
| Logic Error  | After run       | Testing/Debugging|
""")