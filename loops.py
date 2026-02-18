#
# Example file for working with loops
#

def main():
    print("----- While loop -----")
    x = 0
    # A while loop continues executing as long as the condition is True
    # Useful when you don't know the exact number of iterations beforehand
    while x < 5:
        print(x)    # print the current value of x
        x += 1      # increment x by 1

    print("\n----- For loop with range -----")
    # A for loop with range iterates over a sequence of numbers
    # Useful when you know how many times you want to loop
    for x in range(5, 10):  # starts from 5, goes up to 9
        print(x)

    print("\n----- For loop over a collection -----")
    # You can iterate directly over a collection (list, tuple, set, etc.)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)  # prints each day in the list

    print("\n----- For loop with break -----")
    # The break statement exits the loop immediately
    for x in range(5, 10):
        if x == 7:
            print("Breaking at", x)
            break      # stop the loop when x equals 7
        print(x)

    print("\n----- For loop with continue -----")
    # The continue statement skips the current iteration and moves to the next
    for x in range(5, 10):
        if x % 2 == 0:
            continue  # skip even numbers
        print(x)      # prints only odd numbers

    print("\n----- For loop with enumerate -----")
    # enumerate() provides both the index and the value while looping
    for i, day in enumerate(days):
        print(i, day)  # prints index and day

    print("\n----- Loop with else -----")
    # else block in loops executes if the loop completes normally (no break)
    for x in range(3):
        print(x)
    else:
        print("Loop completed without break")

    print("\n----- Nested loops -----")
    # Nested loops are loops inside other loops
    # Useful for iterating over multi-dimensional structures
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"i={i}, j={j}")  # prints all combinations of i and j

if __name__ == "__main__":
    main()