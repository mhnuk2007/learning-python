""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {
    'Aaron': 5556069,
    'Bill': 5559824,
    'Dad': 5552603,
    'David': 5558331,
    'Dillon': 5553538,
    'Jim': 5555547,
    'Mom': 5552603,
    'Olivia': 5556397,
    'Verne': 5555309
}

if __name__ == '__main__':

    # Attempting to access a non-existent key will raise KeyError
    # print(rolodex['Amanda'])  # Uncommenting this would cause an error

    # 1. Add a new friend Amanda
    rolodex['Amanda'] = 5559754
    print("Amanda's number:", rolodex['Amanda'])

    # 2. Update David's number
    print("David's old number:", rolodex['David'])
    rolodex['David'] = 5550902
    print("David's new number:", rolodex['David'])

    # 3. Store multiple numbers for David using a tuple
    rolodex['David'] = (5558331, 5550902)
    print("David's numbers as tuple:", rolodex['David'])

    # 4. Alternative way: store each number with a unique key
    rolodex['David'] = 5558331
    rolodex['David (secondary)'] = 5550902
    print("David's primary number:", rolodex['David'])
    print("David's secondary number:", rolodex['David (secondary)'])

    # 5. Display the entire Rolodex
    print("\nFull Rolodex:")
    for name, number in rolodex.items():
        print(f"{name}: {number}")