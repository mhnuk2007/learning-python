""" looping-collections.py """

def list_loop():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)


def set_loop():
    numbers = {1, 2, 3}
    for number in numbers:
        print(number)


def dictionary_loop():
    person = {"name": "Olivia", "age": 25}
    for key, value in person.items():
        print(key, ":", value)


if __name__ == "__main__":
    list_loop()
    set_loop()
    dictionary_loop()