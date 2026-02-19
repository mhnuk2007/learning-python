"""
A 3-Dimensional Library System
"""

# 2D list of lists - index books by shelf, position
library_2d = [
    ['Python Basics', 'Java Fundamentals', 'C++ Guide'],  # 0th shelf
    ['Data Structures', 'Algorithms'],                     # 1st shelf
    ['Databases', 'Networking', 'Operating Systems']       # 2nd shelf
]

# 3D list of lists of lists - index books by building, shelf, position
library_3d = [
    [   # 0th building
        ['Python Basics', 'Java Fundamentals', 'C++ Guide'],
        ['Data Structures', 'Algorithms'],
        ['Artificial Intelligence', 'Machine Learning']
    ],
    [   # 1st building
        ['Web Development', 'Cloud Computing'],
        ['Cyber Security']
    ],
    [   # 2nd building
        ['Microservices', 'Docker'],
        [],  # Empty shelf
        ['System Design']
    ]
]

""" Demo Commands (with print() functions to show output when run as main script) """
if __name__ == '__main__':

    # ---------------------------------
    # Indexing 2D list
    # ---------------------------------
    print(library_2d)           # Entire 2D library
    print(library_2d[2])        # Books on shelf 2
    print(library_2d[2][1])     # Book on shelf 2, position 1

    # ---------------------------------
    # Indexing 3D list
    # ---------------------------------
    print(library_3d)              # Entire 3D library system
    print(library_3d[0])           # All shelves in building 0
    print(library_3d[0][2])        # Shelf 2 in building 0
    print(library_3d[0][2][1])     # Specific book in building 0, shelf 2, position 1

    # ---------------------------------
    # Accessing all books in the system
    # ---------------------------------
    for building in library_3d:       # iterate buildings
        for shelf in building:        # iterate shelves
            for book in shelf:        # iterate books
                print(book)