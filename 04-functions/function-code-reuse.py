""" A Functional Italian Kitchen """

def boil_and_stir():
    print("Boiling water")
    print("Adding ingredients to the pot")
    print("Stirring occasionally")
    print("Letting it simmer\n")


def make_pasta():
    boil_and_stir()
    pasta = "a warm bowl of pasta"
    return pasta


def make_soup():
    boil_and_stir()
    soup = "a comforting bowl of soup"
    return soup


# Prepare meals for two
lucas_meal = make_pasta()
sophia_meal = make_soup()

print(f"Lucas is having {lucas_meal}\n")
print(f"Sophia is having {sophia_meal}\n")