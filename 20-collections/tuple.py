"""
===========================================
PYTHON TUPLES – COMPLETE REVISION + ADVANCED
===========================================

This program demonstrates:

1. Tuple creation
2. Accessing elements
3. Tuple immutability
4. Tuple operations
5. Tuple unpacking
6. Nested tuples
7. Tuple vs List behavior
8. Named tuple (advanced concept)
"""

# ===========================================
# 1. Creating a Tuple
# ===========================================

# Instead of storing national information in separate variables:
# capital = "Islamabad"
# population = 240
# currency = "PKR"

# We store them in a tuple (ordered & immutable)

pakistan_info = ("Islamabad", 240, "PKR")

print("Original tuple:", pakistan_info)


# ===========================================
# 2. Accessing Elements (Indexing)
# ===========================================

# Tuples use zero-based indexing (like lists)

print("Capital:", pakistan_info[0])
print("Population (millions):", pakistan_info[1])

# Negative indexing
print("Currency:", pakistan_info[-1])


# ===========================================
# 3. Tuple Immutability
# ===========================================

# Tuples are immutable (cannot modify after creation)

# pakistan_info[0] = "Karachi"  # This would raise TypeError

# If modification is needed:
# Convert to list -> modify -> convert back to tuple

temp_list = list(pakistan_info)
temp_list[0] = "Karachi"
pakistan_info = tuple(temp_list)

print("Modified tuple (after conversion):", pakistan_info)


# ===========================================
# 4. Tuple Operations
# ===========================================

# Length
print("Length:", len(pakistan_info))

# Concatenation
additional_info = ("South Asia",)
combined = pakistan_info + additional_info
print("Concatenated tuple:", combined)

# Repetition
repeated = ("A",) * 3
print("Repeated tuple:", repeated)


# ===========================================
# 5. Tuple Unpacking
# ===========================================

# Assign tuple values to variables

capital, population, currency = pakistan_info
print("Unpacked Capital:", capital)
print("Unpacked Population:", population)
print("Unpacked Currency:", currency)

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ===========================================
# 6. Nested Tuples
# ===========================================

countries = (
    ("Pakistan", "Islamabad"),
    ("Turkey", "Ankara"),
    ("Malaysia", "Kuala Lumpur")
)

print("Nested tuple:", countries)

# Access nested values
print("Capital of Turkey:", countries[1][1])


# ===========================================
# 7. Tuple vs List Behavior
# ===========================================

# Tuple inside list (mutable container holding immutable elements)

data = [("Ali", 85), ("Sara", 90)]
print("Original data:", data)

# We can modify list itself
data.append(("John", 78))
print("After append:", data)

# But individual tuple elements cannot be modified directly
# data[0][0] = "Ahmed"  # This would raise TypeError


# ===========================================
# 8. Advanced: Named Tuple
# ===========================================

from collections import namedtuple

# Named tuple improves readability

Country = namedtuple("Country", ["name", "capital", "population"])

pakistan = Country("Pakistan", "Islamabad", 240)

print("Named Tuple:", pakistan)
print("Access by name:", pakistan.capital)
print("Access by index:", pakistan[0])