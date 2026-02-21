"""
==============================================
PYTHON DICTIONARY ITERATION – COMPLETE REVISION
==============================================

This program demonstrates:

1. Basic key iteration
2. Iterating over values
3. Iterating over key-value pairs
4. Using enumerate() with dictionary
5. Reverse iteration
6. Safe modification during iteration
7. Membership testing
8. Dictionary comprehension
9. Sorting dictionary
10. Functional-style transformation
"""

# ===========================================
# 1. Creating the Dictionary
# ===========================================

student_marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Fatima": 88
}

print("Original Dictionary:", student_marks)


# ===========================================
# 2. Iterating Over Keys (Default Behavior)
# ===========================================

# Time Complexity: O(n)

print("\nIterating over keys:")
for student in student_marks:
    print(student)


# ===========================================
# 3. Iterating Over Values
# ===========================================

print("\nIterating over values:")
for marks in student_marks.values():
    print(marks)


# ===========================================
# 4. Iterating Over Key-Value Pairs
# ===========================================

# Most common & recommended approach

print("\nIterating using items():")
for student, marks in student_marks.items():
    print(f"{student} scored {marks}")


# ===========================================
# 5. Using enumerate() with Dictionary
# ===========================================

# enumerate works on items()

print("\nUsing enumerate():")
for index, (student, marks) in enumerate(student_marks.items()):
    print(f"{index} -> {student}: {marks}")


# ===========================================
# 6. Reverse Iteration
# ===========================================

# Python 3.7+ maintains insertion order

print("\nReverse iteration:")
for student in reversed(student_marks):
    print(student, student_marks[student])


# ===========================================
# 7. Safe Modification While Iterating
# ===========================================

# NEVER modify dictionary directly while iterating
# Safe way: iterate over list copy of keys

print("\nSafe deletion during iteration:")
for student in list(student_marks.keys()):
    if student_marks[student] < 80:
        del student_marks[student]

print("After removing marks < 80:", student_marks)


# ===========================================
# 8. Membership Testing
# ===========================================

# O(1) average time (hash table)

print("\nMembership testing:")
if "Ali" in student_marks:
    print("Ali exists in dictionary")


# ===========================================
# 9. Dictionary Comprehension
# ===========================================

# Increase marks by 5

updated_marks = {
    student: marks + 5
    for student, marks in student_marks.items()
}

print("\nUpdated marks (+5):", updated_marks)

# Filter students above 85

high_achievers = {
    student: marks
    for student, marks in student_marks.items()
    if marks > 85
}

print("High achievers:", high_achievers)


# ===========================================
# 10. Sorting Dictionary
# ===========================================

# Sort by marks (ascending)

sorted_by_marks = dict(
    sorted(student_marks.items(), key=lambda item: item[1])
)

print("\nSorted by marks:", sorted_by_marks)

# Sort by student name

sorted_by_name = dict(
    sorted(student_marks.items())
)

print("Sorted by name:", sorted_by_name)


# ===========================================
# 11. Functional Style (map-like behavior)
# ===========================================

# Transform values using dict comprehension
percentage = {
    student: marks / 100
    for student, marks in student_marks.items()
}

print("\nMarks as percentage:", percentage)


# ===========================================
# Summary Notes
# ===========================================

"""
Best Practice Guidelines:

- Use .items() when both key and value are required.
- Use .values() when only values are needed.
- Never modify dictionary during direct iteration.
- Membership testing in dictionary is O(1) average.
- Dictionary maintains insertion order (Python 3.7+).
"""