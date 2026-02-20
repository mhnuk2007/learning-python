""" dict-comprehensions.py - Dict Comprehensions """

# Example: Map fruits to their lengths
fruits = ['apple', 'banana', 'cherry']
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print("Fruit lengths dict:", fruit_dict)

# Example: Numbers to their squares (only odd numbers)
odd_squares_dict = {x: x**2 for x in range(10) if x % 2 != 0}
print("Odd numbers to squares dict:", odd_squares_dict)