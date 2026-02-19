"""Sets and dictionaries basics."""


def demo_sets() -> None:
    numbers = {1, 2, 2, 3, 4}
    print("Unique numbers:", numbers)
    print("Contains 3?", 3 in numbers)

    evens = {2, 4, 6}
    odds = {1, 3, 5}
    print("Union:", evens | odds)
    print("Intersection with {2,3,4}:", evens & {2, 3, 4})


def demo_dictionaries() -> None:
    student_scores = {
        "Asha": 92,
        "Ben": 84,
        "Chloe": 95,
    }

    student_scores["Ben"] = 88
    student_scores["Dina"] = 90

    print("\nStudent scores:")
    for name, score in student_scores.items():
        print(f"- {name}: {score}")

    top_students = {name: score for name, score in student_scores.items() if score >= 90}
    print("Top students:", top_students)


if __name__ == "__main__":
    demo_sets()
    demo_dictionaries()
