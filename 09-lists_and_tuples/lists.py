"""
Parking Cars in a List
Demonstrates common list operations in Python
"""

if __name__ == '__main__':

    # -------------------------------------------------
    # 1. Create the initial list
    # -------------------------------------------------
    row = ['Ford', 'Audi', 'BMW', 'Lexus']
    print("Initial row:", row)

    # -------------------------------------------------
    # 2. Append an item to the end of the list
    # -------------------------------------------------
    row.append('Mercedes')
    print("\nAfter appending Mercedes:", row)

    # Accessing element by index
    print("Element at index 4:", row[4])

    # -------------------------------------------------
    # 3. Replace an element using index assignment
    # -------------------------------------------------
    row[2] = 'Jeep'  # Replace BMW
    print("\nAfter replacing BMW with Jeep:", row)

    # -------------------------------------------------
    # 4. Append another item
    # -------------------------------------------------
    row.append('Honda')
    print("\nAfter appending Honda:", row)

    # -------------------------------------------------
    # 5. Insert an element at a specific position
    # -------------------------------------------------
    row.insert(0, 'Kia')  # Insert at beginning
    print("\nAfter inserting Kia at the front:", row)

    # -------------------------------------------------
    # 6. Find the index of an element
    # -------------------------------------------------
    mercedes_index = row.index('Mercedes')
    print("\nIndex of Mercedes:", mercedes_index)

    # -------------------------------------------------
    # 7. Remove element by index using pop()
    # -------------------------------------------------
    removed_car = row.pop(mercedes_index)
    print("Removed using pop():", removed_car)
    print("Row after pop:", row)

    # -------------------------------------------------
    # 8. Remove element by value using remove()
    # -------------------------------------------------
    row.remove('Lexus')  # Removes first matching value
    print("\nAfter removing Lexus:", row)