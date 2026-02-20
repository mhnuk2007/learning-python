""" error-handling.py """

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except TypeError:
        print("Both inputs must be numbers.")
    else:
        print("Result:", result)
    finally:
        print("Execution complete.\n")


if __name__ == "__main__":
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers(10, "5")