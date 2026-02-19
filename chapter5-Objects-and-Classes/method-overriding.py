""" 
A Garage Full of Classy Vehicles - Demonstrating Method Overriding
"""

# -------------------------------
# Base Vehicle class
# -------------------------------
class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4  # default full tank

    def drive(self):
        """Drive the vehicle, consuming gas."""
        if self.gas > 0:
            self.gas -= 1
            print(f'The {self.color} {self.manufacturer} goes VROOOM!!!')
        else:
            print(f'The {self.color} {self.manufacturer} sputters out of gas...')

# -------------------------------
# Car class inherits Vehicle
# -------------------------------
class Car(Vehicle):
    """Car class with additional features"""
    def radio(self):
        print("Rockin' Tunes!")

    def window(self):
        print('Ahhh... fresh air!')

# -------------------------------
# Electric Car class inherits Car
# Overrides drive() method
# -------------------------------
class ECar(Car):
    """Electric car overrides the drive method"""
    def drive(self):
        """Override: Electric car drives silently and does not consume gas"""
        print(f'The {self.color} {self.manufacturer} goes ssshhh... (eco-friendly)')

# -------------------------------
# Demo Commands
# -------------------------------
if __name__ == '__main__':
    # Standard Car
    my_car = Car('red', 'Mercedes')
    print("\n--- Standard Car Driving ---")
    my_car.drive()  # original drive method
    my_car.radio()
    my_car.window()

    # Electric Car
    my_ecar = ECar('white', 'Nissan')
    print("\n--- Electric Car Driving (Overridden) ---")
    my_ecar.drive()  # overridden drive method
    my_ecar.radio()  # inherited from Car
    my_ecar.window() # inherited from Car

    # Show gas attribute to highlight that overridden method doesn't use gas
    print("\n--- Gas Tank Status ---")
    print(f"Standard Car gas: {my_car.gas}")
    print(f"Electric Car gas: {my_ecar.gas} (unchanged by overridden drive)")