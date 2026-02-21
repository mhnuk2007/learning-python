"""
===========================================
PYTHON DICTIONARIES – COMPLETE REVISION + ADVANCED
===========================================

This program demonstrates:

1. Dictionary creation
2. Accessing values
3. Adding & updating elements
4. Removing elements
5. Dictionary methods
6. Looping through dictionary
7. Nested dictionaries
8. Shallow copy vs Deep copy
9. Dictionary comprehension
"""

# ===========================================
# 1. Creating a Dictionary
# ===========================================

# Instead of storing national symbols in separate variables:
# national_bird = 'Chukar Partridge'
# national_animal = 'Markhor'
# national_flower = 'Jasmine'
# national_fruit = 'Mango'

# We store them in a dictionary (key-value pairs)

pakistan_symbols = {
    'bird': 'Chukar Partridge',
    'animal': 'Markhor',
    'flower': 'Jasmine',
    'fruit': 'Mango',
}

print("Original dictionary:", pakistan_symbols)


# ===========================================
# 2. Accessing Values
# ===========================================

# Direct access using key
print("National Bird:", pakistan_symbols['bird'])

# Safer access using get()
print("National Animal:", pakistan_symbols.get('animal'))

# Default value if key does not exist
print("National Sport:", pakistan_symbols.get('sport', 'Not Defined'))


# ===========================================
# 3. Adding & Updating Elements
# ===========================================

# Adding new key-value pair
pakistan_symbols['sport'] = 'Hockey'
print("After adding sport:", pakistan_symbols)

# Updating existing value
pakistan_symbols['fruit'] = 'Mango (King of Fruits)'
print("After updating fruit:", pakistan_symbols)


# ===========================================
# 4. Removing Elements
# ===========================================

# pop() removes key and returns its value
removed_value = pakistan_symbols.pop('sport')
print("Removed sport:", removed_value)
print("After pop:", pakistan_symbols)

# del removes specific key
del pakistan_symbols['flower']
print("After deleting flower:", pakistan_symbols)

# popitem() removes last inserted item (insertion order preserved in Python 3.7+)
pakistan_symbols['flower'] = 'Jasmine'
print("Before popitem:", pakistan_symbols)
pakistan_symbols.popitem()
print("After popitem:", pakistan_symbols)


# ===========================================
# 5. Dictionary Methods
# ===========================================

print("Keys:", pakistan_symbols.keys())
print("Values:", pakistan_symbols.values())
print("Items:", pakistan_symbols.items())
print("Length:", len(pakistan_symbols))


# ===========================================
# 6. Looping Through Dictionary
# ===========================================

# Loop through keys
for key in pakistan_symbols:
    print("Key:", key)

# Loop through values
for value in pakistan_symbols.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in pakistan_symbols.items():
    print(key, ":", value)


# ===========================================
# 7. Nested Dictionaries
# ===========================================

countries = {
    "Pakistan": {
        "capital": "Islamabad",
        "population_millions": 240,
        "symbols": pakistan_symbols
    }
}

print("Nested dictionary:", countries)

# Access nested value
print("Pakistan capital:", countries["Pakistan"]["capital"])
print("Pakistan national bird:", countries["Pakistan"]["symbols"]["bird"])


# ===========================================
# 8. Shallow Copy vs Deep Copy
# ===========================================

import copy

print("\n--- SHALLOW COPY EXAMPLE ---")

original = {
    "symbols": {
        "bird": "Chukar Partridge",
        "animal": "Markhor"
    }
}

shallow_copy = original.copy()

# Modify nested dictionary
shallow_copy["symbols"]["bird"] = "Modified Bird"

print("Original after shallow modification:", original)
print("Shallow copy:", shallow_copy)

print("\n--- DEEP COPY EXAMPLE ---")

original = {
    "symbols": {
        "bird": "Chukar Partridge",
        "animal": "Markhor"
    }
}

deep_copy = copy.deepcopy(original)

deep_copy["symbols"]["bird"] = "Modified Bird"

print("Original after deep modification:", original)
print("Deep copy:", deep_copy)


# ===========================================
# 9. Dictionary Comprehension
# ===========================================

numbers = [1, 2, 3, 4, 5]

# Create dictionary of number : cube
cubes = {x: x ** 3 for x in numbers}
print("Cubes dictionary:", cubes)

# Conditional comprehension
even_cubes = {x: x ** 3 for x in numbers if x % 2 == 0}
print("Even cubes dictionary:", even_cubes)