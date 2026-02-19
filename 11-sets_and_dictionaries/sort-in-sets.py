""" Sorting Friends into Sets """

# Set of all friends
friends = {'Mark', 'Rae', 'Verne', 'Richard',
           'Aaron', 'David', 'Bruce', 'Garry',
           'Bill', 'Connie', 'Larry', 'Jim',
           'Landon', 'Dillon', 'Frank', 'Tom',
           'Kyle', 'Katy', 'Olivia', 'Brandon'}

# Set of people who live in my zip code
zipcode = {'Jerry', 'Elaine', 'Cindy', 'Verne',
           'Rudolph', 'Bill', 'Olivia', 'Jim',
           'Lindsay', 'Rae', 'Mark', 'Kramer',
           'Landon', 'Newman', 'George'}

# Set of people who play Munchkin
munchkins = {'Steve', 'Jackson', 'Frank', 'Bill',
             'Mark', 'Landon', 'Rae'}

# Set of Olivia's friends
olivia = {'Jim', 'Amanda', 'Verne', 'Nestor'}

if __name__ == '__main__':

    # Step 1: Find friends who live locally
    local_friends = friends.intersection(zipcode)
    print(f'I have {len(local_friends)} local friends named:\n{local_friends}\n')

    # Step 2: Remove friends who play Munchkin
    invite_friends = local_friends.difference(munchkins)
    print(f'I have {len(invite_friends)} friends to invite named:\n{invite_friends}\n')

    # Step 3: Revise the invite list using Olivia's friends (symmetric difference)
    revised_invite = invite_friends.symmetric_difference(olivia)
    print(f'My revised set has {len(revised_invite)} friends named:\n{revised_invite}\n')