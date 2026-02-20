""" specific-exceptions.py """

def get_list_item(items, index):
    try:
        print("Item:", items[index])
    except IndexError:
        print("Index out of range.")
    except TypeError:
        print("Index must be an integer.")


if __name__ == "__main__":
    get_list_item([1, 2, 3], 1)
    get_list_item([1, 2, 3], 10)
    get_list_item([1, 2, 3], "a")