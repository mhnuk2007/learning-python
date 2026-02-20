""" set-comprehensions.py - Set Comprehensions """

# Example: Unique lengths of fruit names
fruits = ['apple', 'banana', 'cherry']
fruit_lengths = {len(fruit) for fruit in fruits}
print("Unique fruit name lengths:", fruit_lengths)

# Example: Filter set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_even_numbers = {x for x in numbers if x % 2 == 0}
print("Unique even numbers:", unique_even_numbers)