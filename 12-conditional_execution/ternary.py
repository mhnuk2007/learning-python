""" ternary.py """

def check_age(age):
    status = "Adult" if age >= 18 else "Minor"
    print(status)


def max_value(a, b):
    maximum = a if a > b else b
    print(f"Max value is {maximum}")


def even_or_odd(number):
    result = "Even" if number % 2 == 0 else "Odd"
    print(result)


if __name__ == "__main__":
    check_age(20)
    max_value(10, 15)
    even_or_odd(7)