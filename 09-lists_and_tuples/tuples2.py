""" A simple coordinate tuple """

# Demo Commands (with print() functions to show output when run as main script)

if __name__ == '__main__':

    coordinates = (10, 20, 30, 'North')  # create tuple
    print(coordinates)                   # display entire tuple
    print(coordinates[1])                # index and display a single element

    # attempt to modify the tuple - this will raise a TypeError
    coordinates[1] = 50