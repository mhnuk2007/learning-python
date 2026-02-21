"""
==============================================
PYTHON STRING COMBINATION & MANIPULATION
==============================================

This program demonstrates:

1. Concatenation
2. join()
3. Repetition
4. Formatting
5. Splitting & restructuring
6. Replacement & cleaning
7. Alignment & padding
8. Practical data transformation
"""

# ===========================================
# 1. String Concatenation
# ===========================================

first_name = "Honey"
last_name = "Chauhan"

full_name = first_name + " " + last_name
print("Concatenation:", full_name)


# ===========================================
# 2. Using join() (Recommended for Multiple Strings)
# ===========================================

words = ["Python", "is", "simple", "and", "powerful"]
sentence = " ".join(words)

print("\nUsing join():", sentence)

# Joining with custom separator
csv_line = ",".join(words)
print("CSV format:", csv_line)


# ===========================================
# 3. String Repetition
# ===========================================

divider = "-" * 30
print("\nRepetition:")
print(divider)


# ===========================================
# 4. String Formatting
# ===========================================

age = 10
city = "Karachi"

# f-string (recommended)
print("\nUsing f-string:")
print(f"My name is {full_name} and I am {age} years old.")

# format() method
print("\nUsing format():")
print("I live in {}.".format(city))

# Old-style formatting
print("\nUsing % formatting:")
print("Age: %d" % age)


# ===========================================
# 5. Splitting & Restructuring
# ===========================================

data = "Honey,Chauhan,10,Karachi"
parts = data.split(",")

print("\nSplit data:", parts)

# Re-structure as readable sentence
formatted = f"{parts[0]} {parts[1]} is {parts[2]} years old and lives in {parts[3]}"
print("Restructured:", formatted)


# ===========================================
# 6. Replacing & Removing Characters
# ===========================================

text = "  Python Programming  "

print("\nOriginal text with spaces:", repr(text))
cleaned = text.strip()
print("After strip():", cleaned)

replaced = cleaned.replace("Programming", "Coding")
print("After replace():", replaced)

# Remove vowels
vowels = "aeiouAEIOU"
no_vowels = "".join(ch for ch in cleaned if ch not in vowels)
print("Without vowels:", no_vowels)


# ===========================================
# 7. Padding & Alignment
# ===========================================

product = "Laptop"
price = 75000

print("\nAlignment & Padding:")
print(product.ljust(15), str(price).rjust(10))
print(product.center(20, "*"))


# ===========================================
# 8. Case Manipulation & Normalization
# ===========================================

email_input = "   USER@Example.COM   "

normalized_email = email_input.strip().lower()

print("\nNormalized email:", normalized_email)


# ===========================================
# 9. Efficient String Building (Best Practice)
# ===========================================

# Inefficient way (avoid in loops):
# result = ""
# for i in range(5):
#     result += str(i)

# Recommended way:
numbers = []
for i in range(5):
    numbers.append(str(i))

result = "".join(numbers)
print("\nEfficient concatenation:", result)


# ===========================================
# Summary Notes
# ===========================================

"""
Best Practices:

- Use join() for combining multiple strings.
- Use f-strings for clean formatting.
- Use strip() to clean user input.
- Avoid repeated string concatenation inside loops.
- Use split() + join() for transformations.
- Strings are immutable.
"""