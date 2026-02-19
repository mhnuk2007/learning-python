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

    # look up Verne's number
    print("Verne's number:", rolodex['Verne'])

    # look at hash value of 'Verne'
    print("Hash value of 'Verne':", hash('Verne'))

    # add a new friend to the rolodex
    rolodex['Katy'] = 5557788
    print("\nAdded Katy:", rolodex)

    # update an existing number
    rolodex['Dad'] = 5559999
    print("\nUpdated Dad's number:", rolodex)

    # remove a friend from the rolodex
    removed = rolodex.pop('Dillon', None)  # safely remove with default
    print(f"\nRemoved Dillon (number {removed}):", rolodex)

    # iterate over keys and values
    print("\nAll friends in the rolodex:")
    for name, number in rolodex.items():
        print(f"{name}: {number}")

    # check if a friend exists
    print("\nIs Olivia in the rolodex?", 'Olivia' in rolodex)