""" random-utilities.py - Random Utilities """

import random

print("Random Utilities:")

# random integer between 1 and 10
rand_int = random.randint(1, 10)
print("Random integer:", rand_int)

# random choice from a list
colors = ['red', 'blue', 'green', 'yellow']
rand_color = random.choice(colors)
print("Random color:", rand_color)

# shuffle a list
deck = ['A', '2', '3', '4', '5']
print("Original deck:", deck)
random.shuffle(deck)
print("Shuffled deck:", deck)

# random sample without replacement
sampled = random.sample(deck, 3)
print("Random sample of 3:", sampled)

# set seed for reproducibility
random.seed(42)
print("Seeded random number:", random.randint(1, 100))