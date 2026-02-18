#
# Advanced conditional examples in Python
#

def main():
    x, y = 10, 100

    # ------------------------
    # 1. Simple if-elif-else
    # ------------------------
    if x < y:
        print("x is less than y")      # Output: x is less than y
    elif x == y:
        print("x equals y")
    else:
        print("x is greater than y")

    # ------------------------
    # 2. Ternary / conditional expression
    # ------------------------
    result = "x < y" if x < y else "x >= y"
    print(result)                      # Output: x < y

    registered_user = True
    access_level = "admin" if registered_user else "guest"
    print("You have access as", access_level)                # Output: admin


    # ------------------------
    # 3. Nested conditions
    # ------------------------
    age = 20
    citizen = True

    if age >= 18:
        if citizen:
            print("Eligible to vote")  # Output: Eligible to vote
        else:
            print("Not a citizen")
    else:
        print("Too young to vote")

    # ------------------------
    # 4. Multiple conditions with logical operators
    # ------------------------
    score = 85
    passed = True

    if score > 80 and passed:
        print("Great job!")           # Output: Great job!

    if score > 90 or not passed:
        print("Needs improvement")
    else:
        print("Keep going!")          # Output: Keep going!

    # ------------------------
    # 5. Membership conditions
    # ------------------------
    fruits = ["apple", "banana", "mango"]
    fruit = "banana"

    if fruit in fruits:
        print(f"{fruit} is available")  # Output: banana is available

    if "grape" not in fruits:
        print("Grape is not available") # Output: Grape is not available

    # ------------------------
    # 6. Python 3.10 match-case (like switch)
    # ------------------------
    value = "two"

    match value:
        case "one":
            result = 1
        case "two":
            result = 2                  # Output: 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)

    # ------------------------
    # 7. Conditional with multiple expressions
    # ------------------------
    a, b, c = 5, 10, 5
    if a == b:
        print("a equals b")
    elif a == c:
        print("a equals c")             # Output: a equals c
    else:
        print("No matches")

if __name__ == "__main__":
    main()