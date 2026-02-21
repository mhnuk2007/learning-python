"""
===========================================
PYTHON LISTS – COMPLETE REVISION + ADVANCED
===========================================

This program demonstrates:

1. List creation
2. Indexing (positive & negative)
3. Slicing
4. Mutability
5. Adding & removing elements
6. Sorting & reversing
7. Memory behavior (reference model)
8. Shallow copy vs Deep copy (real difference)
9. Nested lists
10. List comprehension (advanced concept)
"""

# ===========================================
# 1. Creating a List
# ===========================================

# Instead of storing cities in separate variables,
# we store them in a single list (better scalability)

capitals = ["Karachi", "Lahore", "Peshawar", "Quetta"]

print("Original List:", capitals)


# ===========================================
# 2. Accessing Elements (Indexing)
# ===========================================

# Python uses zero-based indexing

print("First city:", capitals[0])      
print("Second city:", capitals[1])     

# Negative indexing (access from end)
print("Last city:", capitals[-1])      
print("Second last city:", capitals[-2])  


# ===========================================
# 3. List Slicing
# ===========================================

# Syntax: list[start:end]  (end is excluded)

print("First two:", capitals[0:2])
print("Middle slice:", capitals[1:3])
print("From start to index 2:", capitals[:2])
print("From index 2 to end:", capitals[2:])

# Reverse using slicing (creates new list)
print("Reversed using slicing:", capitals[::-1])


# ===========================================
# 4. Modifying a List (Mutability)
# ===========================================

# Lists are mutable (can change after creation)

capitals[0] = "Islamabad"
print("After modification:", capitals)


# ===========================================
# 5. Adding Elements
# ===========================================

# append() adds at end (O(1) average time complexity)
capitals.append("Karachi")
print("After append:", capitals)

# insert(index, value) shifts elements (O(n))
capitals.insert(1, "Gilgit")
print("After insert:", capitals)


# ===========================================
# 6. Removing Elements
# ===========================================

# remove(value) removes first matching value
capitals.remove("Gilgit")
print("After remove:", capitals)

# del removes by index
del capitals[0]
print("After del:", capitals)

# pop() removes and returns last element
removed_city = capitals.pop()
print("Popped city:", removed_city)
print("After pop:", capitals)


# ===========================================
# 7. Sorting & Reversing
# ===========================================

# sort() modifies original list
capitals.sort()
print("Sorted list:", capitals)

# reverse() modifies original list
capitals.reverse()
print("Reversed list:", capitals)

# sorted() returns new sorted list (safer approach)
sorted_copy = sorted(capitals)
print("Sorted copy:", sorted_copy)

print("Length of list:", len(capitals))

num_list = [5, 2, 9, 1]
print("Original numbers:", num_list)
print("Sorted numbers:", sorted(num_list))



# ===========================================
# 8. Memory Behavior (Reference Model)
# ===========================================

# Lists store references, not raw values

a = [1, 2, 3]
b = a  # Both variables reference the same list object

print("a:", a)
print("b:", b)
b.append(4)

print("a after modifying b:", a)  
print("b:", b)


# ===========================================
# 9. Shallow Copy vs Deep Copy
# ===========================================

import copy

print("\n--- SHALLOW COPY EXAMPLE (Nested List) ---")

# Nested list (2D list)
a = [[1, 2], [3, 4]]

# Shallow copy (outer list copied, inner lists shared)
b = a[:]

print("a before modification:", a)
print("b:", b)

# Modify inner list
b[0].append(99)

print("a after shallow copy modification:", a)
print("b:", b)

print("\n--- DEEP COPY EXAMPLE ---")

a = [[1, 2], [3, 4]]

# Deep copy creates fully independent structure
b = copy.deepcopy(a)

print("a before modification:", a)
print("b:", b)

b[0].append(99)

print("a after deep copy modification:", a)
print("b:", b)


# ===========================================
# 10. Nested Lists + While Loop
# ===========================================

students_marks = [
    [80, 75, 90],
    [60, 70, 65],
    [88, 92, 85]
]

totals = []
i = 0

while i < len(students_marks):
    j = 0
    total = 0

    while j < len(students_marks[i]):
        total += students_marks[i][j]
        j += 1

    totals.append(total)
    i += 1

print("Total marks of each student:", totals)


# ===========================================
# 11. Advanced: List Comprehension
# ===========================================

numbers = [1, 2, 3, 4, 5]

# Square each number
squares = [x * x for x in numbers]
print("Squares:", squares)

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Flatten 2D list
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)