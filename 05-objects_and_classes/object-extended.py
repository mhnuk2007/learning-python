""" What Makes Up an Object? (Extended Version) """

# -------------------------------------------------
# Examine a string object
# -------------------------------------------------
print('shirt')
print(type('shirt'))
print(dir('shirt'))

# Use upper method on a string object
print('shirt'.upper())

# Examine IDs of different string objects
print(id('shirt'))
print(id('pants'))

# -------------------------------------------------
# Examine an integer object
# -------------------------------------------------
print(id(1))
print(dir(1))

# -------------------------------------------------
# Examine ID and attributes of built-in functions
# -------------------------------------------------
print(id(id))
print(dir(dir))

# -------------------------------------------------
# Examine a list object
# -------------------------------------------------
numbers = [1, 2, 3]
print(numbers)
print(type(numbers))
print(dir(numbers))
print(id(numbers))

# Modify list (shows mutability)
numbers.append(4)
print(numbers)

# -------------------------------------------------
# Examine a dictionary object
# -------------------------------------------------
person = {"name": "Alice", "age": 30}
print(person)
print(type(person))
print(dir(person))
print(id(person))

# -------------------------------------------------
# Create and examine a custom class
# -------------------------------------------------
class Shirt:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def describe(self):
        return f"{self.color} shirt, size {self.size}"


my_shirt = Shirt("blue", "M")

print(my_shirt)
print(type(my_shirt))
print(dir(my_shirt))
print(id(my_shirt))

# Inspect instance attributes
print(my_shirt.__dict__)

# Call a method
print(my_shirt.describe())

# -------------------------------------------------
# Functions are objects too
# -------------------------------------------------
def greet(name):
    return f"Hello {name}"

print(type(greet))
print(dir(greet))
print(greet.__name__)
print(greet.__dict__)   # functions also have attribute storage