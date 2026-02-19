""" Adding and Removing Friends from Sets """

# Revised set of friends to invite
invite = {'Nestor', 'Amanda', 'Olivia'}

if __name__ == '__main__':

    # Check if Verne is already invited
    print('Is Verne invited?', 'Verne' in invite)

    # Invite Verne
    invite.add('Verne')
    print('After inviting Verne:', invite)

    # Ensure Olivia is invited (idempotent)
    invite.add('Olivia')
    print('After ensuring Olivia is invited:', invite)

    # Remove Nestor from the invite list
    invite.remove('Nestor')
    print('After removing Nestor:', invite)
    # invite.remove('Nestor')  # would throw KeyError if uncommented

    # Start inviting friends (pop elements one by one)
    while invite:
        print('Inviting:', invite.pop())

    # Attempt to pop from empty set safely
    if not invite:
        print('No more friends left to invite.')