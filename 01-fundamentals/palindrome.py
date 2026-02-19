# Palindrome Checker

import string  # for removing punctuation

def is_palindrome(teststr):
    # 1. Convert to lowercase
    cleanedstr = teststr.lower()
    
    # 2. Remove spaces and punctuation
    cleanedstr = "".join(c for c in cleanedstr if c.isalnum())
    
    # 3. Reverse string
    reversestr = cleanedstr[::-1]
    
    # 4. Compare original cleaned string with reversed string
    return cleanedstr == reversestr

# List of test words/phrases
test_words = ["Hello World!", "Radar", "Mama?", "Madam, I'm Adam.", "Race car!"]

# Check each word and count total palindromes
total = 0
for word in test_words:
    if is_palindrome(word):
        total += 1
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is NOT a palindrome")

print(f"Total palindromes: {total}")