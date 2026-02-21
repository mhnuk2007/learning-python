"""
==============================================
PYTHON STRINGS – COMPLETE REVISION
==============================================

This program demonstrates:

1. String creation
2. Indexing & slicing
3. Iteration
4. String methods
5. Searching & replacing
6. Splitting & joining
7. Formatting
8. Validation methods
9. Immutability concept
"""

# ===========================================
# 1. Creating Strings
# ===========================================

name = "Honey Chauhan"
message = "  Welcome to Python Programming  "

print("Original name:", name)
print("Original message:", message)


# ===========================================
# 2. Indexing & Slicing
# ===========================================

print("\nIndexing:")
print("First character:", name[0])
print("Last character:", name[-1])

print("\nSlicing:")
print("First 8 chars:", name[:8])
print("Last 3 chars:", name[-3:])
print("Reversed string:", name[::-1])


# ===========================================
# 3. Iterating Over String
# ===========================================

print("\nIterating using for loop:")
for ch in name:
    print(ch)

print("\nIterating using enumerate:")
for index, ch in enumerate(name):
    print(f"{index} -> {ch}")


# ===========================================
# 4. Common String Methods
# ===========================================

print("\nCase conversion:")
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())

print("\nWhitespace handling:")
print("Stripped message:", message.strip())

print("\nLength:")
print("Length of name:", len(name))


# ===========================================
# 5. Searching & Replacing
# ===========================================

print("\nSearching:")
print("Index of 'Chauhan':", name.find("Chauhan"))
print("Contains 'Chauhan'?", "Chauhan" in name)

print("\nReplacing:")
new_name = name.replace("Honey", "Honey")
print("After replace:", new_name)


# ===========================================
# 6. Splitting & Joining
# ===========================================

sentence = "Python is simple and powerful"

words = sentence.split()
print("\nSplit into words:", words)

joined = "-".join(words)
print("Joined with hyphen:", joined)


# ===========================================
# 7. String Formatting
# ===========================================

age = 10
city = "Karachi"

# f-string (recommended)
print("\nUsing f-string:")
print(f"My name is {name} and I am {age} years old.")

# format() method
print("\nUsing format():")
print("I live in {}.".format(city))


# ===========================================
# 8. Validation Methods
# ===========================================

username = "user123"
print("\nValidation checks:")
print("Is alphanumeric?", username.isalnum())
print("Is alphabetic?", username.isalpha())
print("Is digit?", username.isdigit())

email = "test@example.com"
print("Contains '@'?", "@" in email)


# ===========================================
# 9. String Immutability
# ===========================================

# Strings are immutable

text = "Hello"
# text[0] = "h"  # This would cause an error

# Correct way:
modified_text = "h" + text[1:]
print("\nModified text:", modified_text)


# ===========================================
# 10. Counting & Advanced Usage
# ===========================================

paragraph = "Python is easy. Python is readable. Python is powerful."

print("\nCount occurrences of 'Python':", paragraph.count("Python"))

# Remove vowels example
vowels = "aeiouAEIOU"
no_vowels = "".join(ch for ch in paragraph if ch not in vowels)
print("Without vowels:", no_vowels)


# ===========================================
# Summary Notes
# ===========================================

"""
Best Practice Guidelines:

- Strings are immutable.
- Use f-strings for formatting (cleanest approach).
- Use strip() to clean input data.
- Use split() + join() for transformations.
- Membership test is O(n).
- Strings support slicing like lists.
"""