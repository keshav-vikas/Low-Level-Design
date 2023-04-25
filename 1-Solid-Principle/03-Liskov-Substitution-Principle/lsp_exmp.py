'''
Liskov Substitution Principle (LSP): Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
'''
# Violation of LSP
from abc import ABC, abstractmethod
import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


'''
In this example, we have a Rectangle class with a set_width and set_height method that sets the width and height of the rectangle. We also have a Square class
that inherits from Rectangle, and overrides the set_width and set_height methods to ensure that the width and height are always equal (since a square has equal
sides).

However, this violates the Liskov Substitution Principle because a Square object cannot be substituted for a Rectangle object. If we create a Square object 
and try to set its width and height separately, we'll end up with a square that is no longer square:
'''


def print_area(rectangle):
    rectangle.set_width(4)
    rectangle.set_height(5)
    area = rectangle.area()
    print(f"Area: {area}")


square = Square(3)
print_area(square)  # Prints "Area: 12" (incorrect)

'''
This violates the Liskov Substitution Principle because a Square object should be able to be substituted for a Rectangle object without affecting the
correctness of the program.
'''

# Following LSP


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2


def print_area(shape):
    print("Area: ", shape.get_area())


# create a rectangle object
rectangle = Rectangle(3, 4)

# create a square object
square = Square(2)

# pass the objects to print_area function
print_area(rectangle)
print_area(square)

'''
In this example, we have defined an abstract base class Shape that defines an abstract method get_area(). The Rectangle and Square classes implement 
this method to return the area of the respective shape. This ensures that any subclass of Shape can be used in place of a Shape object without breaking 
the contract of the Shape class.
'''

# OR


class Shape:
    def area(self):
        pass


class Quadrilateral(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Rectangle(Quadrilateral):
    pass


class Square(Quadrilateral):
    def __init__(self, length):
        super().__init__(length, length)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def get_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area


# Client code
shapes = [Rectangle(5, 4), Square(5), Circle(5)]
total_area = get_total_area(shapes)
print(total_area)

'''
In this example, Quadrilateral class is created as a base class for Rectangle and Square classes, which inherit the area() method from Quadrilateral.

The Square class overrides the __init__() method to take only one parameter for the length, and it calculates the area of the square based on that.

The Circle class is created as a separate class and it implements the area() method in a way that is different from the Quadrilateral subclasses.

The get_total_area() function takes a list of Shape objects and calculates the total area by calling the area() method on each of them. This function can work
with any subclass of Shape, including Rectangle, Square, and Circle, without knowing anything about their internal implementations.

This code follows the Liskov Substitution Principle because each subclass of Shape can be used in place of its parent class without affecting the correctness 
of the program. In other words, the get_total_area() function can work with any object that implements the area() method, regardless of its specific subclass.
'''
