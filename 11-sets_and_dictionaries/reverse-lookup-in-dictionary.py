""" A Rolodex Full of Friends with Reverse Lookup """

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

def caller_id(lookup_number):
    """
    Returns a list of names associated with a given phone number.
    Returns None if the number is not found.
    """
    matches = [name for name, number in rolodex.items() if number == lookup_number]
    if matches:
        return matches
    else:
        return None

# Demo Commands (with print() functions to show output when run as main script)
if __name__ == '__main__':

    # reverse-lookup Olivia's number
    print("Lookup 5556397:", caller_id(5556397))

    # reverse-lookup a number not in the rolodex
    print("Lookup 8675309:", caller_id(8675309))

    # reverse-lookup number shared by Dad & Mom
    print("Lookup 5552603:", caller_id(5552603))