""" multiple-exceptions.py - Multiple Exceptions Together """

def risky_operations(a, b):
    try:
        result = a / b
        items = [1, 2, 3]
        print(items[a])
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
    except Exception as e:
        print("Some other error:", e)
    else:
        print("Result:", result)
    finally:
        print("Operation finished.\n")


if __name__ == "__main__":
    risky_operations(1, 0)
    risky_operations(5, 2)
    risky_operations(2, 2)