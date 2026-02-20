""" loop-control.py """

def break_example():
    print("Break example:")
    for i in range(10):
        if i == 5:
            break
        print(i)


def continue_example():
    print("\nContinue example:")
    for i in range(5):
        if i == 2:
            continue
        print(i)


def pass_example():
    print("\nPass example:")
    for i in range(3):
        if i == 1:
            pass
        print(i)


if __name__ == "__main__":
    break_example()
    continue_example()
    pass_example()