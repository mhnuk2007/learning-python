""" Inheritance Example: Animals """

# -------------------------------------------------
# Base Animal class
# -------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Generic speak method"""
        print(f"{self.name} makes a sound.")

# -------------------------------------------------
# Dog subclass inherits Animal
# -------------------------------------------------
class Dog(Animal):
    def speak(self):
        """Override speak for Dog"""
        print(f"{self.name} barks: Woof!")

# -------------------------------------------------
# Cat subclass inherits Animal
# -------------------------------------------------
class Cat(Animal):
    def speak(self):
        """Override speak for Cat"""
        print(f"{self.name} meows: Meow!")

# -------------------------------------------------
# Demo
# -------------------------------------------------
if __name__ == '__main__':
    # create animal objects
    generic_animal = Animal("Generic")
    my_dog = Dog("Buddy")
    my_cat = Cat("Whiskers")

    # demonstrate inheritance and overriding
    generic_animal.speak()  # calls Animal's speak
    my_dog.speak()          # calls Dog's speak
    my_cat.speak()          # calls Cat's speak

    # check types and isinstance
    print(isinstance(my_dog, Animal))  # True
    print(isinstance(my_cat, Animal))  # True
    print(isinstance(generic_animal, Dog))  # False