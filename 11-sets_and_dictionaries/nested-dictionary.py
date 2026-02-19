""" Friends Contact Manager """

# dictionary of friends with nested dictionaries for multiple details
friends = {
    'Aaron': {'phone': 5556069, 'email': 'aaron@example.com', 'city': 'New York'},
    'Olivia': {'phone': 5556397, 'email': 'olivia@example.com', 'city': 'Los Angeles'},
    'Jim': {'phone': 5555547, 'email': 'jim@example.com', 'city': 'Chicago'},
    'Verne': {'phone': 5555309, 'email': 'verne@example.com', 'city': 'Miami'},
}

if __name__ == '__main__':

    # 1. Access a friend's email
    print("Olivia's email:", friends['Olivia']['email'])

    # 2. Add a new friend
    friends['Katy'] = {'phone': 5557788, 'email': 'katy@example.com', 'city': 'Boston'}
    print("\nAdded Katy:", friends)

    # 3. Update a friend's city
    friends['Jim']['city'] = 'San Francisco'
    print("\nUpdated Jim's city:", friends['Jim'])

    # 4. Remove a friend
    removed = friends.pop('Aaron', None)
    print(f"\nRemoved Aaron: {removed}")
    print("Current friends:", friends)

    # 5. Print all friends in a formatted way
    print("\nAll friends:")
    for name, details in friends.items():
        print(f"{name} -> Phone: {details['phone']}, Email: {details['email']}, City: {details['city']}")

    # 6. Find friends in a specific city
    city = 'Los Angeles'
    la_friends = [name for name, details in friends.items() if details['city'] == city]
    print(f"\nFriends in {city}:", la_friends)

    # 7. Check if a friend exists
    print("\nIs Verne in friends?", 'Verne' in friends)