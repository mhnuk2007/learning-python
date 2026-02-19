""" A Stack of Books to Read """

# Demo Commands (with print() functions to show output when run as main script)

if __name__ == '__main__':

    # create a list to use as the stack
    stack = []

    # add some books to the stack
    stack.append('Book1')
    stack.append('Book2')

    # read the top book (LIFO)
    print(stack.pop())

    # add two more books
    stack.append('Book3')
    stack.append('Book4')

    # read books from top to bottom
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # attempting to pop from an empty stack
    try:
        stack.pop()
    except IndexError:
        print("Stack is empty")