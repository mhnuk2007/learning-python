"""
==============================================
PYTHON STRING PATTERN SEARCHING
==============================================

This program demonstrates:

1. Basic pattern search
2. Counting patterns
3. startswith / endswith
4. Case-insensitive search
5. Regular expressions (re module)
6. Extracting structured data
"""

import re

# ===========================================
# 1. Basic Pattern Search
# ===========================================

text = "Python is powerful. Python is easy. Python is popular."

print("Original Text:")
print(text)

print("\nBasic search using 'in':")
print("Contains 'Python'?", "Python" in text)

print("\nUsing find():")
print("First occurrence index:", text.find("Python"))

print("\nUsing rfind():")
print("Last occurrence index:", text.rfind("Python"))


# ===========================================
# 2. Counting Occurrences
# ===========================================

count = text.count("Python")
print("\nNumber of occurrences:", count)


# ===========================================
# 3. startswith() and endswith()
# ===========================================

print("\nStarts with 'Python'?", text.startswith("Python"))
print("Ends with 'popular.'?", text.endswith("popular."))


# ===========================================
# 4. Case-Insensitive Search
# ===========================================

text2 = "python is fun"

print("\nCase-insensitive search:")
print("Contains 'Python'?", "python" in text2.lower())


# ===========================================
# 5. Regular Expressions (Advanced Pattern Matching)
# ===========================================

data = """
Contact us at support@example.com
or admin@test.org.
Call 123-456-7890 or 9876543210.
"""

print("\nExtracting emails using regex:")
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", data)
print(emails)

print("\nExtracting phone numbers:")
phones = re.findall(r"\d{3}-\d{3}-\d{4}|\d{10}", data)
print(phones)


# ===========================================
# 6. Extracting Words Starting with Capital Letter
# ===========================================

sentence = "Ali and Sara went to Lahore and Islamabad."

capital_words = re.findall(r"\b[A-Z][a-z]+\b", sentence)
print("\nWords starting with capital letter:", capital_words)


# ===========================================
# 7. Replacing Patterns
# ===========================================

print("\nReplacing phone numbers with [HIDDEN]:")
masked_data = re.sub(r"\d{3}-\d{3}-\d{4}|\d{10}", "[HIDDEN]", data)
print(masked_data)


# ===========================================
# 8. Validating Email Format
# ===========================================

email = "test123@gmail.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("\nValid email format")
else:
    print("\nInvalid email format")


# ===========================================
# Summary Notes
# ===========================================

"""
Key Concepts:

- 'in' → simplest substring check
- find() → returns index (or -1)
- count() → count occurrences
- startswith() / endswith()
- re.findall() → extract all matches
- re.sub() → replace patterns
- re.match() → validate pattern at start
"""