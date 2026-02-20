""" functools-utilities.py - Functools Utilities """

from functools import reduce, lru_cache

print("Functools Utilities:")

nums = [1, 2, 3, 4, 5]

# reduce to sum all numbers
total = reduce(lambda x, y: x + y, nums)
print("Sum via reduce:", total)

# reduce to find product
product = reduce(lambda x, y: x * y, nums)
print("Product via reduce:", product)

# cached property / memoization
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci numbers:")
for i in range(10):
    print(fib(i), end=" ")
print()