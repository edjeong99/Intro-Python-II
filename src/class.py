'''
class WheeledVehicle:   # "Base class", "Super class", "Parent class"
    def __init__(self, name, num_wheels):
        self.name = name
        self.num_wheels = num_wheels

    def drive(self):
        print(f"{self.name} is driving!")


# "Derived class", "specialized", "sub class", "child class"
class Motorcycle(WheeledVehicle):
    def __init__(self, name):
        super().__init__(name, 2)

    def drive(self):     # Method overriding
        super().drive()
        print("Brrraaaapp!")


class Car(WheeledVehicle):
    def __init__(self, name):
        super().__init__(name, 4)


c = Car("Adventuremobile")  # c is an instance of Car

c.drive()

m = Motorcycle("Jackie")

m.drive()

# Dynamically add new method to base class


def new_function(self):
    print("Hi!")


WheeledVehicle.fn = new_function

m.fn()
c.fn()
'''

# Method Resolution Order (MRO)


class Animal():
    def move(self):
        print("animal move")


class Jumper():
    def move(self):
        print("jumper move")

    def jump():
        pass


class Grasshopper(Animal, Jumper):
    pass


class Kangaroo(Animal, Jumper):
    pass


class Octopus(Animal):
    pass


g = Grasshopper()

g.move()
