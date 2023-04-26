'''
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them
 into a separate class, and make their objects interchangeable.
Strategy Pattern is a design pattern that enables our application to select algorithms at runtime,
 making our application flexible.

'''
'''
class Vehicle:
    def __init__(self):
        pass

    def drive(self):
        print("normal drive capability")


class SportsCar(Vehicle):
    def drive(self):
        print("special drive capability")


class PassengerVehicle(Vehicle):
    #print("normal drive capability")
    pass


class OffloadVehicle(Vehicle):
    def drive(self):
        print("special drive capability")


# Problem
# both the sibling(SportsCar, OffloadVehicle) need the same function which is not present in 
# base class , here we are duplicating the code
'''

# Solution
#  create Strategy Interface for drive




from abc import ABC, abstractmethod
class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("normal drive capability")


class SpecialDriveStrategy(DriveStrategy):
    def drive(self):
        print("special drive strategy")


# use of has a relationship
class Vehicle:

    # construction injection
    def __init__(self, driveObject):
        self.driveObject = driveObject

    def drive(self):
        self.driveObject.drive()


class OffloadVehicle(Vehicle):

    def __init__(self):
        super().__init__(SpecialDriveStrategy())


d1 = OffloadVehicle()
d1.drive()
