""" combining-tools.py - Combining Tools """

import random
import itertools

print("Combining random and itertools:")

deck = ['A', '2', '3', '4', '5', '6']
random.shuffle(deck)
hands = list(itertools.combinations(deck, 2))
print("Two-card hands from shuffled deck:", hands[:5])