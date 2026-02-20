""" custom-exception.py """

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    print("Valid age.")


if __name__ == "__main__":
    try:
        check_age(-5)
    except InvalidAgeError as e:
        print("Custom Error:", e)