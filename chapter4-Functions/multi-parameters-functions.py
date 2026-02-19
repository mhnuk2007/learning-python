""" A Functional Burger Bar """

def grill_and_assemble():
    print('Grilling the patty')
    print('Toasting the bun')
    print('Adding the base ingredients')
    print('Assembling the burger')
    print('Wrapping it up\n')


def make_burger(cheese):
    grill_and_assemble()
    burger = f'a burger with {cheese}'
    return burger


def make_classic_burger():
    grill_and_assemble()
    burger = 'a classic cheeseburger'
    return burger


def make_deluxe_burger(*toppings):
    grill_and_assemble()
    burger = f'a deluxe burger with {len(toppings)} extra toppings'
    return burger


# make meals for two
ethan_meal = make_burger('cheddar cheese')
mia_meal = make_deluxe_burger('bacon', 'avocado', 'fried egg',
                              'caramelized onions', 'jalapeños')

print(f'Ethan is having {ethan_meal}\n')
print(f'Mia is having {mia_meal}\n')