class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.enginetype = enginetype
        self.doors = 4
        self.wheels = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print(f"Car is driving at {self.speed} mph with a {self.enginetype} engine.")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        self.enginetype = enginetype
        self.doors = 0
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print(f"Motorcycle is driving at {self.speed} mph with a {self.enginetype} engine.")

car1  = Car("gas")
car2  = Car("electric")
mc1 = Motorcycle("gas", True)

print(car1.enginetype)
print(car2.doors)
print(mc1.wheels)

car1.drive(30)
car2.drive(50)
mc1.drive(40)

print(car1.speed)
print(mc1.speed)
print(car2.speed)
print(car1.enginetype)
print(mc1.enginetype)
print(car2.enginetype)