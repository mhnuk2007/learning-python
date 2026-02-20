""" loop-else.py """

def search_number(numbers, target):
    for number in numbers:
        if number == target:
            print("Found:", target)
            break
    else:
        print("Not found:", target)


if __name__ == "__main__":
    search_number([1, 2, 3, 4], 3)
    search_number([1, 2, 3, 4], 9)