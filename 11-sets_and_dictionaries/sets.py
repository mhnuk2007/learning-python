""" Creating and Combining Sets of Friends """

# Sets of friends by category
college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

if __name__ == '__main__':

    # Display the college set
    print("College friends:", college)

    # Number of friends in each set
    print("Number of college friends:", len(college))
    print("Number of coworkers:", len(coworker))
    print("Number of family friends:", len(family))

    # Combine all friends into a single set (union)
    all_friends = college.union(coworker, family)
    print("\nAll friends combined:", all_friends)
    print("Total unique friends:", len(all_friends))

    # Find friends who are in both college and coworker sets (intersection)
    college_and_coworker = college.intersection(coworker)
    print("\nFriends both in college and coworker sets:", college_and_coworker)

    # Find friends who are only in college (difference)
    only_college = college.difference(coworker, family)
    print("Friends only in college:", only_college)

    # Symmetric difference: friends in college or family but not both
    exclusive_friends = college.symmetric_difference(family)
    print("Friends either in college or family but not both:", exclusive_friends)