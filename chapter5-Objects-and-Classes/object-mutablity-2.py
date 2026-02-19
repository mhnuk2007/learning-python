""" Pets and Their Toys """

# -------------------------
# Mutable object: list of toys
# -------------------------
dog_toys = ['ball', 'bone', 'rope']
cat_toys = dog_toys  # another reference to the same list

print("Dog toys:", dog_toys)
print("Cat toys:", cat_toys)
print("Are dog_toys and cat_toys the same object?", dog_toys is cat_toys)

# Add a new toy for the dog
dog_toys.append('frisbee')
print("\nAfter adding a toy to dog_toys:")
print("Dog toys:", dog_toys)
print("Cat toys:", cat_toys)  # cat_toys sees the change
print("Are dog_toys and cat_toys still the same object?", dog_toys is cat_toys)

# -------------------------
# Immutable object: pet names
# -------------------------
dog_name = "Rex"
cat_name = dog_name  # another reference to the same string

print("\nInitial names:")
print("Dog:", dog_name)
print("Cat:", cat_name)
print("Are dog_name and cat_name the same object?", dog_name is cat_name)

# Change the dog's name
dog_name = "Buddy"
print("\nAfter changing dog's name:")
print("Dog:", dog_name)
print("Cat:", cat_name)
print("Are dog_name and cat_name still the same object?", dog_name is cat_name)