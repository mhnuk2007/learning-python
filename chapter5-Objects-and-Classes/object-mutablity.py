""" You Can Change an Outfit, But You Can't Change Your Words """

# Demo Commands (showing mutability of lists vs immutability of strings)

# -------------------------
# Mutable object example: list
# -------------------------
closet = ['shirt', 'hat', 'pants', 'jacket', 'socks']
print("Initial closet:", closet)
print("ID of closet:", id(closet))

# remove a hat (list is mutable)
closet.remove('hat')
print("Closet after removing hat:", closet)
print("ID of closet after modification:", id(closet))  # same ID

# add a new item
closet.append('scarf')
print("Closet after adding scarf:", closet)
print("ID of closet after adding item:", id(closet))   # same ID

# -------------------------
# Immutable object example: string
# -------------------------
words = "You're wearing that"
print("\nInitial words:", words)
print("ID of words:", id(words))

# concatenate string (creates a new string object)
words = words + " because you look great!"
print("Words after adding more:", words)
print("ID of words after concatenation:", id(words))  # new ID

# -------------------------
# Takeaways
# -------------------------
print("\nTakeaways:")
print("Lists are mutable → modifying in place doesn't change the object ID")
print("Strings are immutable → modifying creates a new object with a new ID")