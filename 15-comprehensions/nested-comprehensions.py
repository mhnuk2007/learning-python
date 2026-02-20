""" nested-comprehensions.py - Nested Comprehensions """

# Flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print("Flattened matrix:", flat_list)

# Nested comprehension with condition
even_flat_list = [num for row in matrix for num in row if num % 2 == 0]
print("Flattened even numbers:", even_flat_list)