#
# Example file for working with functions
# Python practice for Java developers
#

# ------------------------
# 1. Basic function
# ------------------------
def hello_world():
    print("Hello, World!")

hello_world()  # Output: Hello, World!

# ------------------------
# 2. Function with parameters
# ------------------------
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                       # Output: Hello, Alice!
greet("Bob", "Hi")                   # Output: Hi, Bob!
greet(name="Charlie", greeting="Hey")# Output: Hey, Charlie!

# ------------------------
# 3. Function that returns a value
# ------------------------
def cube(x):
    return x ** 3

result = cube(3)
print(result)  # Output: 27

# ------------------------
# 4. Function with default argument
# ------------------------
def power(base, exponent=2):
    return base ** exponent

print(power(2))       # Output: 4 (2^2)
print(power(2, 3))    # Output: 8 (2^3)
print(power(exponent=4, base=3))  # Output: 81 (3^4)

# ------------------------
# 5. Function with variable number of arguments
# ------------------------
def multi_add(start, *args):
    result = start
    for num in args:
        result += num
    return result

print(multi_add(10, 4, 5, 10, 4))  # Output: 33
print(multi_add(0, 1, 2, 3))       # Output: 6

# ------------------------
# 6. Functions as first-class objects
# ------------------------
def say_hello():
    return "Hello!"

greet_func = say_hello   # Assign function to a variable
print(greet_func())      # Output: Hello!