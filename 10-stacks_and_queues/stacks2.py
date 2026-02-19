""" A Stack of Bills to Pay """

# Demo Commands (with print() functions to show output when run as main script)

if __name__ == '__main__':

    # create a list to use as the stack
    stack = []
    print("Initial stack:", stack)

    # add some bills to the stack (push)
    stack.append('bill1')
    stack.append('bill2')
    print("After adding bill1 and bill2:", stack)

    # remove the top bill to pay it (pop)
    paid_bill = stack.pop()
    print("Paid:", paid_bill)
    print("Stack after payment:", stack)

    # add two more bills
    stack.append('bill3')
    stack.append('bill4')
    print("After adding bill3 and bill4:", stack)

    # remove bills from top to bottom (LIFO order)
    while stack:
        print("Paying:", stack.pop())

    print("Stack after clearing:", stack)

    # demonstrate safe pop from empty stack
    try:
        stack.pop()
    except IndexError:
        print("Cannot pop: stack is empty")