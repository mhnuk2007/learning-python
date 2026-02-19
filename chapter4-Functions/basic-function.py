""" A Functional Pancake Shop """

def make_pancakes():
    print("Mixing flour, milk, and eggs")
    print("Heating the pan")
    print("Pouring the batter")
    print("Flipping the pancake")
    print("Cooking until golden brown\n")
    
    pancakes = "a stack of fluffy pancakes"
    return pancakes


# Make breakfast for two
emma_breakfast = make_pancakes()
liam_breakfast = make_pancakes()

print(f"Emma is having {emma_breakfast}\n")
print(f"Liam is having {liam_breakfast}\n")