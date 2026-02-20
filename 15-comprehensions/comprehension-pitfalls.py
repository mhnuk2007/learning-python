""" comprehension-pitfalls.py - Common Pitfalls """

# Avoid overly complex one-liners
# Hard to read:
# result = [x**2 if x % 2 == 0 else x**3 for x in range(10)]
# Better split into readable loops if complex logic

# Prefer clarity over cleverness
for x in range(10):
    if x % 2 == 0:
        print(f"{x} squared is {x**2}")