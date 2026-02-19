""" Two Pets, One Toy """

class Toy:
    def __init__(self, name):
        self.name = name
        self.is_clean = True  # attribute to track if toy is clean

    def make_dirty(self):
        self.is_clean = False

    def make_clean(self):
        self.is_clean = True


if __name__ == '__main__':

    # create one toy and assign it to two pets
    ball = Toy('Ball')
    kitty_ball = ball  # kitty_ball references the same toy as ball

    # examine IDs (memory addresses)
    print("Ball ID:", id(ball))
    print("Kitty Ball ID:", id(kitty_ball))
    print("Ball is clean?", ball.is_clean)
    print("Kitty Ball is clean?", kitty_ball.is_clean)

    # cat plays with the toy, making it dirty
    kitty_ball.make_dirty()
    print("\nAfter cat plays with the toy:")
    print("Ball is clean?", ball.is_clean)       # False
    print("Kitty Ball is clean?", kitty_ball.is_clean)  # False

    # check if they reference the same object
    print("Are ball and kitty_ball the same object?", ball is kitty_ball)

    # dog gets a new toy
    dog_ball = Toy('Ball')
    print("\nNew toy for dog created:")
    print("Ball ID:", id(ball))
    print("Dog Ball ID:", id(dog_ball))
    print("Dog Ball is clean?", dog_ball.is_clean)
    print("Ball is clean?", ball.is_clean)

    # clean the old toy
    ball.make_clean()
    print("\nAfter cleaning the original toy:")
    print("Ball is clean?", ball.is_clean)
    print("Dog Ball is clean?", dog_ball.is_clean)

    # check object identity again
    print("Are ball and dog_ball the same object?", ball is dog_ball)