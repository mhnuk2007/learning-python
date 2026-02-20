""" loops.py """

def for_loop_example():
    print("For loop example:")
    for i in range(5):
        print(i)


def while_loop_example():
    print("\nWhile loop example:")
    count = 0
    while count < 5:
        print(count)
        count += 1


if __name__ == "__main__":
    for_loop_example()
    while_loop_example()