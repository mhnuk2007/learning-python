""" Two Names, One Shirt """

class Shirt:
    def __init__(self):
        self.clean = True  # attribute to track if the shirt is clean

    def make_dirty(self):
        self.clean = False  # mark the shirt as dirty

    def make_clean(self):
        self.clean = True   # mark the shirt as clean


if __name__ == '__main__':

    # create one shirt and assign it to two variables
    red = Shirt()
    crimson = red  # crimson references the same object as red

    # examine their IDs (memory addresses)
    print(id(red))      # e.g., 140302323678864
    print(id(crimson))  # same as red
    print(red.clean)    # True
    print(crimson.clean)  # True

    # make the shirt dirty via red
    red.make_dirty()
    print(red.clean)      # False
    print(crimson.clean)  # False, because both point to same object

    # check if they are the exact same object
    print(red is crimson)  # True

    # create a second Shirt object and assign it to crimson
    crimson = Shirt()  # now crimson references a new object

    # examine IDs
    print(id(red))      # old shirt
    print(id(crimson))  # new shirt, different ID
    print(crimson.clean)  # True, new shirt starts clean
    print(red.clean)      # False, old shirt is still dirty

    # clean the red shirt
    red.make_clean()
    print(red.clean)      # True
    print(crimson.clean)  # True (new shirt was already clean)

    # check if they are still the same object
    print(red is crimson)  # False