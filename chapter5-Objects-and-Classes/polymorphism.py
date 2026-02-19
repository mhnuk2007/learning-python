""" Polymorphism Example: Animals """

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Demo
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()  # same method name, different behavior depending on object