""" A Garage Full of Classy Vehicles """

# -------------------------------------------------
# Base class Vehicle
# Contains attributes and behaviors common to all vehicles
# -------------------------------------------------
class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color                  # Vehicle color
        self.manufacturer = manufacturer    # Vehicle brand/maker
        self.gas = 4                        # Full tank of gas (default 4 units)

    def drive(self):
        """Simulate driving the vehicle and consume gas"""
        if self.gas > 0:
            self.gas -= 1
            print(f'The {self.color} {self.manufacturer} goes VROOOM!!!')
        else:
            print(f'The {self.color} {self.manufacturer} sputters out of gas...')

# -------------------------------------------------
# Car class inherits from Vehicle
# Adds specific behaviors for cars
# -------------------------------------------------
class Car(Vehicle):
    def radio(self):
        """Turn on the car radio"""
        print("Rockin' Tunes!")

    def window(self):
        """Open the car window"""
        print('Ahhh... fresh air!')

# -------------------------------------------------
# Motorcycle class inherits from Vehicle
# Adds specific behaviors for motorcycles
# -------------------------------------------------
class Motorcycle(Vehicle):
    def helmet(self):
        """Put on a helmet before riding"""
        print('Helmet on - nice and safe!')


# -------------------------------------------------
# Demo commands to test inheritance and behaviors
# -------------------------------------------------
if __name__ == '__main__':
    
    # Create instances of Car and Motorcycle
    my_car = Car('red', 'Mercedes')
    my_mc = Motorcycle('silver', 'Harley')

    # Drive them and see gas consumption in action
    my_car.drive()       # Mercedes drives
    my_mc.drive()        # Harley drives
    my_mc.drive()
    my_mc.drive()
    my_mc.drive()
    my_mc.drive()        # Out of gas
    my_car.drive()       # Mercedes drives again

    # Demonstrate subclass-specific behaviors
    my_car.radio()       # Only cars can use radio
    my_car.window()      # Only cars can open windows
    my_mc.helmet()       # Only motorcycles use helmets

    # Attempting my_mc.window() would raise an AttributeError
    # because Motorcycle does not have a window() method