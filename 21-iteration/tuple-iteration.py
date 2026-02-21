"""
==============================================
PYTHON TUPLE ITERATION – COMPLETE REVISION
==============================================

This program demonstrates:

1. Basic iteration
2. Index-based iteration
3. enumerate() usage
4. Reverse iteration
5. Nested tuple iteration
6. Tuple unpacking
7. Membership testing
8. Generator expression (tuple-style processing)
9. Sorting tuples
"""

# ===========================================
# 1. Creating the Tuple
# ===========================================

fruits = (
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes"
)

print("Original Tuple:", fruits)


# ===========================================
# 2. Basic Iteration (for loop)
# ===========================================

print("\nIterating using for loop:")
for fruit in fruits:
    print(fruit)


# ===========================================
# 3. Index-Based Iteration (while loop)
# ===========================================

print("\nIterating using while loop:")
i = 0
while i < len(fruits):
    print(f"Index {i}: {fruits[i]}")
    i += 1


# ===========================================
# 4. Using enumerate()
# ===========================================

print("\nIterating using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"{index} -> {fruit}")


# ===========================================
# 5. Reverse Iteration
# ===========================================

print("\nReverse iteration using reversed():")
for fruit in reversed(fruits):
    print(fruit)

print("\nReverse iteration using index:")
i = len(fruits) - 1
while i >= 0:
    print(fruits[i])
    i -= 1


# ===========================================
# 6. Nested Tuple Iteration
# ===========================================

employees = (
    ("Ali", "Developer", 80000),
    ("Sara", "Manager", 95000),
    ("John", "Designer", 70000)
)

print("\nNested tuple iteration:")
for employee in employees:
    print(employee)

print("\nNested tuple unpacking:")
for name, role, salary in employees:
    print(f"{name} works as {role} earning {salary}")


# ===========================================
# 7. Tuple Unpacking
# ===========================================

coordinates = (25.2048, 55.2708)
latitude, longitude = coordinates

print("\nLatitude:", latitude)
print("Longitude:", longitude)


# ===========================================
# 8. Membership Testing
# ===========================================

print("\nMembership testing:")
if "Mango" in fruits:
    print("Mango exists in tuple")


# ===========================================
# 9. Generator Expression (Tuple Processing)
# ===========================================

# Tuples do not support comprehension directly like lists,
# but we can use generator expressions.

uppercase_fruits = tuple(fruit.upper() for fruit in fruits)
print("\nUppercase fruits:", uppercase_fruits)

long_named = tuple(fruit for fruit in fruits if len(fruit) > 5)
print("Fruits with name length > 5:", long_named)


# ===========================================
# 10. Sorting Tuples
# ===========================================

numbers = (5, 2, 9, 1, 7)

sorted_numbers = tuple(sorted(numbers))
print("\nSorted numbers:", sorted_numbers)

# Sorting nested tuples by salary
sorted_employees = tuple(
    sorted(employees, key=lambda emp: emp[2])
)

print("Employees sorted by salary:", sorted_employees)


# ===========================================
# Summary Notes
# ===========================================

"""
Best Practice Guidelines:

- Tuples are immutable (cannot modify elements).
- Iteration is O(n).
- Use unpacking for cleaner nested tuple handling.
- Use tuple() + generator expression for transformation.
- Ideal for fixed, read-only structured data.
"""