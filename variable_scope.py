# --------------------------------------
# Scope of Variables in Python (LEGB Rule)
# LEGB = Local, Enclosing, Global, Built-in
# --------------------------------------

print("\n--- Local Scope Example ---")
# Local: Variables defined inside a function are only accessible there
def local_example():
    local_var = "I am local"
    print("Inside function:", local_var)

local_example()
# print(local_var)  # Error: local_var is not accessible outside

print("\n--- Enclosing (Nonlocal) Scope Example ---")
# Enclosing: Variables in the outer function accessible to inner function
def outer_function():
    enclosing_var = "I am enclosing"
    
    def inner_function():
        nonlocal enclosing_var  # Allows modification of enclosing_var
        enclosing_var += " (modified by inner)"
        print("Inside inner function:", enclosing_var)
    
    inner_function()
    print("Inside outer function:", enclosing_var)

outer_function()

print("\n--- Global Scope Example ---")
# Global: Variables defined outside all functions
global_var = "I am global"

def read_global():
    print("Reading global variable:", global_var)  # Reading works without 'global'

def modify_global():
    global global_var  # Needed to modify global variable
    global_var += " (modified)"
    print("Modified inside function:", global_var)

read_global()
modify_global()
print("Global variable outside function:", global_var)

print("\n--- Built-in Scope Example ---")
# Built-in: Python provides built-in functions and constants
print("Length of 'Hello':", len("Hello"))        # len() is built-in
print("Absolute of -10:", abs(-10))             # abs() is built-in
print("Maximum of [3,5,1]:", max(3, 5, 1))      # max() is built-in
print("Minimum of [3,5,1]:", min(3, 5, 1))      # min() is built-in
print("Type of 42:", type(42))                  # type() is built-in

# --------------------------------------
# Notes:
# - Local: exists only inside the function
# - Enclosing: exists in outer function, accessible to inner function
# - Global: exists in the module, accessible everywhere in the module
# - Built-in: Python's predefined functions and constants, accessible anywhere
# --------------------------------------