""" conditionals.py """

def evaluate_number(number):
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


def check_grade(score):
    if score >= 90:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")


def compare_values(a, b):
    if a == b:
        print("Equal")
    elif a != b and a > b:
        print("A is greater than B")
    else:
        print("A is less than B")


if __name__ == "__main__":
    evaluate_number(10)
    evaluate_number(-5)
    evaluate_number(0)

    check_grade(85)

    compare_values(7, 3)