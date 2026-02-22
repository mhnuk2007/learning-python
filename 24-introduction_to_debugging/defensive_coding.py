"""
========================================
DEFENSIVE CODING – BEST PRACTICES
========================================

This program demonstrates defensive coding techniques
to prevent bugs before they occur.
"""

print("=== DEFENSIVE CODING DEMO ===\n")

# =========================================
# 1. Validating User Input
# =========================================

print("1. Input Validation")

def get_age():
    """Safely get age from user."""
    age_input = input("Enter your age: ")
    
    if age_input.isdigit():
        age = int(age_input)
        if 0 <= age <= 150:
            return age
        else:
            print("Age must be between 0 and 150")
            return None
    else:
        print("Please enter a valid number")
        return None

# Example usage (commented for auto-run)
# age = get_age()
# print(f"Valid age: {age}")

print("   Input validation prevents runtime errors\n")

# =========================================
# 2. Checking Before Operations
# =========================================

print("2. Pre-operation Checks")

def safe_divide(a, b):
    """Divide safely with check."""
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, None

result, error = safe_divide(10, 0)
if error:
    print(f"   Error: {error}")
else:
    print(f"   Result: {result}")

def safe_list_access(items, index):
    """Access list safely."""
    if 0 <= index < len(items):
        return items[index]
    return None

items = [1, 2, 3]
print(f"   items[5] safely: {safe_list_access(items, 5)}\n")

# =========================================
# 3. Using Assertions
# =========================================

print("3. Assertions for Development")

def calculate_average(numbers):
    """Calculate average with assertions."""
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) > 0, "List cannot be empty"
    
    return sum(numbers) / len(numbers)

# This works
avg = calculate_average([10, 20, 30])
print(f"   Average: {avg}")

# This would raise AssertionError (commented)
# avg = calculate_average([])

print("   Assertions catch logic errors during development\n")

# =========================================
# 4. Type Checking
# =========================================

print("4. Type Checking")

def add_numbers(a, b):
    """Add two numbers with type checking."""
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number, got {type(b).__name__}")
    
    return a + b

try:
    result = add_numbers(5, "hello")
except TypeError as e:
    print(f"   Caught: {e}")

print()

# =========================================
# 5. Default Values
# =========================================

print("5. Default Values")

def greet(name=None):
    """Greet with default value."""
    if name is None:
        name = "Guest"
    return f"Hello, {name}!"

print(f"   {greet()}")
print(f"   {greet('Ali')}\n")

# =========================================
# 6. Early Returns
# =========================================

print("6. Early Returns (Guard Clauses)")

def process_data(data):
    """Process data with early returns."""
    if data is None:
        return "No data provided"
    
    if not isinstance(data, list):
        return "Data must be a list"
    
    if len(data) == 0:
        return "Data list is empty"
    
    # Main logic here
    return f"Processed {len(data)} items"

print(f"   None: {process_data(None)}")
print(f"   String: {process_data('hello')}")
print(f"   Empty: {process_data([])}")
print(f"   Valid: {process_data([1, 2, 3])}\n")

# =========================================
# Summary
# =========================================

print("=== DEFENSIVE CODING CHECKLIST ===")
print("""
✅ Validate all user input
✅ Check before operations (division, index access)
✅ Use assertions during development
✅ Check types when necessary
✅ Provide sensible defaults
✅ Return early for invalid cases
✅ Handle exceptions gracefully
✅ Write clear error messages
""")