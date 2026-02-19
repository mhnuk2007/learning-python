""" Tracking Hobbies with Sets """

# Sets of hobbies for three friends
alice_hobbies = {'reading', 'swimming', 'gaming', 'painting'}
bob_hobbies = {'gaming', 'cycling', 'swimming', 'cooking'}
carol_hobbies = {'painting', 'yoga', 'reading', 'cooking'}

if __name__ == '__main__':

    # Display each friend's hobbies
    print("Alice's hobbies:", alice_hobbies)
    print("Bob's hobbies:", bob_hobbies)
    print("Carol's hobbies:", carol_hobbies)

    # Hobbies shared by Alice and Bob
    common_alice_bob = alice_hobbies.intersection(bob_hobbies)
    print("\nHobbies Alice and Bob share:", common_alice_bob)

    # Hobbies that are unique to Carol
    unique_carol = carol_hobbies.difference(alice_hobbies, bob_hobbies)
    print("Hobbies unique to Carol:", unique_carol)

    # All hobbies from all friends (union)
    all_hobbies = alice_hobbies.union(bob_hobbies, carol_hobbies)
    print("All hobbies combined:", all_hobbies)

    # Hobbies that are exclusive to only one friend (symmetric difference)
    exclusive_hobbies = alice_hobbies.symmetric_difference(bob_hobbies).symmetric_difference(carol_hobbies)
    print("Hobbies that are unique to one friend:", exclusive_hobbies)