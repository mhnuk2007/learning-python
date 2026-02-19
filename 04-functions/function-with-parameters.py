""" A Functional Pizza Kitchen """

def prepare_and_bake(topping):
    print("Preparing the dough")
    print("Spreading tomato sauce")
    print(f"Adding {topping}")
    print("Placing pizza in the oven")
    print("Baking until golden and crispy\n")


def make_pizza(topping):
    prepare_and_bake(topping)
    return f"a {topping} pizza"


def make_calzone(filling):
    prepare_and_bake(filling)
    return f"a {filling} calzone"


# Make meals for two
noah_meal = make_pizza("pepperoni")
ava_meal = make_calzone("spinach and cheese")

print(f"Noah is having {noah_meal}\n")
print(f"Ava is having {ava_meal}\n")