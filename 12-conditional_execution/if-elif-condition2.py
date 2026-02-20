""" Ordering A Pizza That Verne Can Eat """

# things that Verne does not eat
diet_restrictions = {'meat', 'cheese'}

if 'meat' in diet_restrictions and 'cheese' in diet_restrictions:
    print('Get a vegan pizza.')

elif 'meat' in diet_restrictions:
    print('Get a cheese pizza.')

elif 'cheese' in diet_restrictions:
    print('Get a veggie pizza without cheese.')

else:
    print('Order any pizza you like.')