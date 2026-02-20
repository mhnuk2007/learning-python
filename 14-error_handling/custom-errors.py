"""Custom exception examples."""


class InvalidAgeError(ValueError):
    """Raised when age is out of allowed range."""


def validate_age(age: int) -> int:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 120:
        raise InvalidAgeError("Age seems unrealistic")
    return age


if __name__ == "__main__":
    samples = [22, -5, 180]

    for value in samples:
        try:
            print(f"Validating age: {value}")
            result = validate_age(value)
            print("Valid age:", result)
        except InvalidAgeError as exc:
            print("Validation error:", exc)
