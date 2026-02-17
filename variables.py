# Basic datatypes in Python: Numbers, Strings and Booleans
# Variable names start with a letter or an underscore, followed by letters, digits or underscores. They are case-sensitive.
# Examples of variable names: my_variable, _myVariable, myVariable2

# Numbers
myint = 10
myfloat = 7.5

# Strings
mystr = "Hello, World!"
another_str = 'Python is great!'
_new_str = "It's a nice day!"  # Using double quotes to include a single quote

# Booleans
mybool = True
another_bool = False

# Printing variables
print(myint)        # Output: 10
print(myfloat)      # Output: 7.5
print(mystr)        # Output: Hello, World!
print(another_str)  # Output: Python is great!
print(_new_str)     # Output: It's a nice day!
print(mybool)       # Output: True
print(another_bool) # Output: False

# Operations on variables
result = myint + myfloat
print(result)       # Output: 17.5
greeting = mystr + " " + another_str
print(greeting)     # Output: Hello, World! Python is great!

# Logical and Comparison operations
is_greater = myint > myfloat
print(is_greater)       # Output: True

print(myint == 10)      # Output: True
print(myint == 10.0)    # Output: True (int and float comparison)

print(myfloat != 20)    # Output: True
print(mybool and another_bool)  # Output: False
print(mybool or another_bool)   # Output: True

print(myint > 5 and myfloat < 10)  # Output: True

# Variable redeclaration and reassignment
myint = 20
print(myint)       # Output: 20

myint = "JavaScript"
print(myint)       # Output: JavaScript



