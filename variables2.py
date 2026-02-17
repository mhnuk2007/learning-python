# Advanced Data Structures in Python: Lists, Tuples, Dictionaries, Sets

# -------------------------
# LISTS: Ordered, mutable, allows duplicates
# -------------------------
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)      # [1, 2, 3, 4, 5]

# Operations on lists
my_list.append(6)
print("After append:", my_list)       # [1, 2, 3, 4, 5, 6]

my_list.remove(3)
print("After remove 3:", my_list)     # [1, 2, 4, 5, 6]

print("First element:", my_list[0])   # 1
print("Last element:", my_list[-1])   # 6
print("Slicing 1:4:", my_list[1:4])   # [2, 4, 5]

# Reverse list
print("Reversed list:", my_list[::-1])  # [6, 5, 4, 2, 1]
my_list.reverse()
print("Reversed in place:", my_list)    # [6, 5, 4, 2, 1]

# -------------------------
# TUPLES: Ordered, immutable, allows duplicates
# -------------------------
my_tuple = (1, 2, 5, 3, 4, 5)
print("Tuple:", my_tuple)

# Access elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Reverse tuple
reversed_tuple = my_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

# -------------------------
# SETS: Unordered, mutable, no duplicates
# -------------------------
my_set = {1, 2, 3, 3, 4, 5}
print("Set (duplicates removed):", my_set)

# Add and remove
my_set.add(6)
my_set.remove(2)
print("Updated set:", my_set)

# Sets are unordered, convert to list to reverse
reversed_set_list = sorted(my_set, reverse=True)
print("Reversed set as list:", reversed_set_list)

# -------------------------
# DICTIONARIES: Unordered, mutable, key-value pairs
# -------------------------
my_dict = {"name": "Honey", "age": 10}
print("Dictionary:", my_dict)

# Access values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Reverse dictionary items
reversed_items = dict(reversed(list(my_dict.items())))
print("Dictionary with reversed items:", reversed_items)

# Loop through dictionary in reverse (keys)
for key in reversed(list(my_dict.keys())):
    print(f"{key} => {my_dict[key]}")