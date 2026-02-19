""" The Blueprints for Vehicles """

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.running = False

    def start(self):
        print(f'{self.year} {self.make} {self.model} is starting')
        self.running = True

    def stop(self):
        print(f'{self.year} {self.make} {self.model} is stopping')
        self.running = False


class Car(Vehicle):
    def honk(self):
        print(f'{self.make} {self.model} goes: Beep Beep!')


class Motorcycle(Vehicle):
    def rev_engine(self):
        print(f'{self.make} {self.model} goes: Vroom Vroom!')


# Demo Commands
if __name__ == '__main__':
    # Create a Car
    my_car = Car('Toyota', 'Corolla', 2022)
    print(type(my_car))
    print(dir(my_car))

    my_car.start()
    print(my_car.running)
    my_car.honk()

    # Create a Motorcycle
    my_bike = Motorcycle('Yamaha', 'R15', 2021)
    print(type(my_bike))
    print(dir(my_bike))

    my_bike.start()
    print(my_bike.running)
    my_bike.rev_engine()

    # Stop vehicles
    my_car.stop()
    print(my_car.running)
    my_bike.stop()
    print(my_bike.running)