diet_restrictions = {'meat', 'cheese'}

if {'meat', 'cheese'}.issubset(diet_restrictions):
    print('Get a vegan pizza.')

elif 'meat' in diet_restrictions:
    print('Get a cheese pizza.')

else:
    print('Regular pizza is fine.')