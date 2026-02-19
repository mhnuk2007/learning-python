""" Managing Students in a Classroom """

# Demo Commands (with print() functions to show output when run as main script)

if __name__ == '__main__':

    # create the initial list of students
    classroom = ['Alice', 'Bob', 'Charlie', 'Diana']
    print(classroom)

    # add Ethan to the end of the list
    classroom.append('Ethan')
    print(classroom)
    print(classroom[4])  # student at index 4

    # replace Charlie (index 2) with Frank
    classroom[2] = 'Frank'
    print(classroom)

    # add Grace to the end
    classroom.append('Grace')
    print(classroom)
    print(classroom[4])  # element at index 4 (after changes)

    # insert Henry at the beginning
    classroom.insert(0, 'Henry')
    print(classroom)
    print(classroom[4])  # observe how index positions shift

    # find Ethan’s index and remove using pop()
    ethan_index = classroom.index('Ethan')
    print(ethan_index)
    print(classroom.pop(ethan_index))
    print(classroom)

    # remove Diana by value
    classroom.remove('Diana')
    print(classroom)