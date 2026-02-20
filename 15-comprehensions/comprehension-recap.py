""" comprehension-recap.py - Quick Recap Example """

import math

# Input list
numbers = [1, 2, 3, 4, 5, 6]

# List comprehension with filter
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print("Squared evens:", squared_evens)

# Dict comprehension mapping number to boolean (even/odd)
even_odd_map = {x: (x % 2 == 0) for x in numbers}
print("Even/odd mapping:", even_odd_map)

# Set comprehension of square roots (just integer parts)
sqrt_set = {math.isqrt(x) for x in numbers}
print("Integer square roots set:", sqrt_set)