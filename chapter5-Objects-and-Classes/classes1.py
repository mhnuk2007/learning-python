""" The Blueprints for Animals """

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.awake = False

    def wake_up(self):
        print(f'{self.name} is waking up')
        self.awake = True

    def sleep(self):
        print(f'{self.name} is going to sleep')
        self.awake = False


class Dog(Animal):
    def bark(self):
        print(f'{self.name} says: Woof!')


class Cat(Animal):
    def meow(self):
        print(f'{self.name} says: Meow!')


# Demo Commands (with print() functions to show output when run as main script)
if __name__ == '__main__':

    # create and examine a dog
    my_dog = Dog('Buddy', 3)
    print(type(my_dog))
    print(dir(my_dog))

    # wake up and interact
    my_dog.wake_up()
    print(my_dog.awake)
    my_dog.bark()

    # create and examine a cat
    my_cat = Cat('Whiskers', 2)
    print(type(my_cat))
    print(dir(my_cat))

    # wake up and interact
    my_cat.wake_up()
    print(my_cat.awake)
    my_cat.meow()

    # put animals to sleep
    my_dog.sleep()
    print(my_dog.awake)

    my_cat.sleep()
    print(my_cat.awake)