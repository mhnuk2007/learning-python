""" Exploring What Makes Up an Object """

# Examine a list object
print([1, 2, 3])
print(type([1, 2, 3]))
print(dir([1, 2, 3]))

# Use a method on a list object
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# Examine IDs of different list objects
print(id([1, 2, 3]))
print(id([4, 5, 6]))

# Examine a dictionary object
print({"name": "Alice"})
print(type({"name": "Alice"}))
print(dir({"name": "Alice"}))

# Examine ID and attributes of built-in functions
print(id(len))
print(dir(len))

# Examine a custom function object
def greet():
    return "Hello!"

print(id(greet))
print(dir(greet))