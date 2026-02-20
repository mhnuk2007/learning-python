""" list-comprehensions.py - List Comprehensions """

# Example: Square numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Example: Square only even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Example: Convert strings to uppercase
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)