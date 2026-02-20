""" assertions.py """

def calculate_square_root(number):
    assert number >= 0, "Number must be non-negative."
    return number ** 0.5


if __name__ == "__main__":
    print(calculate_square_root(16))
    print(calculate_square_root(-4))