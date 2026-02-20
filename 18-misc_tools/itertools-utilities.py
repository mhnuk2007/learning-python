""" itertools-utilities.py - Itertools Utilities """

import itertools

print("Itertools Utilities:")

numbers = [1, 2, 3]
letters = ['a', 'b']

# Cartesian product
prod = list(itertools.product(numbers, letters))
print("Product:", prod)

# permutations
perm = list(itertools.permutations(numbers))
print("Permutations:", perm)

# combinations
comb = list(itertools.combinations(numbers, 2))
print("Combinations:", comb)

# count, cycle, repeat
counter = itertools.count(start=5, step=5)
print("First 5 counts:", [next(counter) for _ in range(5)])

cycler = itertools.cycle(['X', 'Y'])
print("First 6 cycles:", [next(cycler) for _ in range(6)])

repeater = itertools.repeat('Hello', 3)
print("Repeater:", list(repeater))