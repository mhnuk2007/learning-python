""" A Functional Pizza Kitchen """

sauce = 'tomato'

def prepare_and_bake():
    print('Rolling the dough')
    print('Spreading the sauce')
    print('Adding toppings')
    print('Baking in the oven')
    print('Slicing the pizza\n')


def make_regular_pizza():
    prepare_and_bake()
    pizza = f'a pizza with {sauce} sauce'
    return pizza


def make_special_pizza():
    global sauce
    sauce = 'pesto'
    prepare_and_bake()
    pizza = f'a special pizza with {sauce} sauce'
    return pizza


# Make meals
print(f'*** global sauce is {sauce} ***\n')

alex_meal = make_regular_pizza()
print(f'*** global sauce is {sauce} ***\n')

emma_meal = make_special_pizza()
print(f'*** global sauce is {sauce} ***\n')

print(f'Alex is having {alex_meal}\n')
print(f'Emma is having {emma_meal}\n')