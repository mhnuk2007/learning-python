"""
===========================================
PYTHON LIST ITERATION – COMPLETE REVISION
===========================================

This program demonstrates:

1. Basic iteration (for loop)
2. Index-based iteration (while loop)
3. enumerate() usage
4. Reverse iteration
5. Iterating over a copy (safe modification)
6. List comprehension usage
7. Membership testing
"""

# ===========================================
# 1. Creating the List
# ===========================================

capitals = [
    "Islamabad",
    "Karachi",
    "Lahore",
    "Peshawar",
    "Quetta"
]

print("Original List:", capitals)


# ===========================================
# 2. Iterating Using for Loop (Recommended Way)
# ===========================================

# Clean and Pythonic
# Time Complexity: O(n)

print("\nIterating using for loop:")
for city in capitals:
    print(city)

spices  =[
    "Cumin",
    "Turmeric",
    "Coriander",
    "black pepper"
]
print("\nIterating over spices:")
for spice in spices:
    print(spice)
print("Delicious omlete with these spices!!!")


# ===========================================
# 3. Iterating Using while Loop (Index-Based)
# ===========================================

# Useful when manual index control is required

print("\nIterating using while loop:")
i = 0
while i < len(capitals):
    print(f"Index {i}: {capitals[i]}")
    i += 1

i = 5
while i <= 100:
    print(i)
    i += 5


# ===========================================
# 4. Iterating Using enumerate()
# ===========================================

# enumerate() provides both index and value
# More readable than manual indexing

print("\nIterating using enumerate:")
for index, city in enumerate(capitals):
    print(f"Index: {index}, City: {city}")


# ===========================================
# 5. Reverse Iteration
# ===========================================

print("\nReverse iteration using reversed():")
for city in reversed(capitals):
    print(city)

print("\nReverse iteration using index (while loop):")
i = len(capitals) - 1
while i >= 0:
    print(capitals[i])
    i -= 1


# ===========================================
# 6. Iterating Over a Copy (Safe Modification)
# ===========================================

# Modifying a list while iterating can cause logical issues.
# Safe approach: iterate over a copy.

print("\nSafe modification while iterating:")
for city in capitals[:]:   # shallow copy
    if city == "Karachi":
        capitals.remove(city)

print("After removing Karachi safely:", capitals)


# Restore original list
capitals.append("Karachi")


# ===========================================
# 7. Membership Testing
# ===========================================

# O(n) operation for list

print("\nMembership testing:")
if "Lahore" in capitals:
    print("Lahore exists in the list")


# ===========================================
# 8. List Comprehension (Advanced & Pythonic)
# ===========================================

# Transforming data
uppercase_capitals = [city.upper() for city in capitals]
print("\nUppercase version:", uppercase_capitals)

# Filtering data
cities_with_a = [city for city in capitals if "a" in city.lower()]
print("Cities containing letter 'a':", cities_with_a)


# ===========================================
# 9. Sorting with Custom Key
# ===========================================

# Sort by length of city name
sorted_by_length = sorted(capitals, key=len)
print("\nSorted by name length:", sorted_by_length)


# ===========================================
# 10. Functional Style Iteration (map)
# ===========================================

# Using map() to transform data
lowercase_capitals = list(map(str.lower, capitals))
print("Lowercase using map():", lowercase_capitals)


# ===========================================
# Summary Notes
# ===========================================

"""
Best Practice Guidelines:

- Prefer 'for city in list' for clean iteration.
- Use enumerate() when index is required.
- Avoid modifying a list while iterating over it directly.
- Use list comprehension for transformation/filtering.
- Remember membership test in list is O(n).
"""