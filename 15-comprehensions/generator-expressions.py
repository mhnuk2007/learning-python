""" generator-expressions.py - Generator Expressions """

# Example: Lazy sequence of squares
square_gen = (x**2 for x in range(10))  # does not create full list
print("Generator object:", square_gen)
print("First item:", next(square_gen))
print("Remaining items:", list(square_gen))

# Example: Sum of squares using generator
sum_squares = sum(x**2 for x in range(10))
print("Sum of squares:", sum_squares)