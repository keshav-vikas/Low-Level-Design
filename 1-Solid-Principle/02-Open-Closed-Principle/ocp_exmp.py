'''
Open-Closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
'''
# Bad example: A class that violates the OCP
from abc import ABC, abstractmethod
import math


class Shape:
    def __init__(self, type):
        self.type = type

    def area(self):
        if self.type == 'rectangle':
            return self.width * self.height
        elif self.type == 'circle':
            return self.radius ** 2 * math.pi

    # This method violates the OCP
    def draw(self):
        if self.type == 'rectangle':
            # code to draw a rectangle
            pass
        elif self.type == 'circle':
            # code to draw a circle
            pass


'''
In the bad example, the Shape class violates the Open-Closed Principle because the draw method checks the type of the shape and performs different actions depending on the type. This means that the class is not closed for modification because it needs to be modified every time a new type of shape is added.

'''

# Good example: A class that follows the OCP


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


class ShapeDrawer:
    def draw(self, shape):
        print(shape.draw())


class RectangleDrawer(ShapeDrawer):
    def draw(self, shape):
        return "Drawing rectangle with width = {}, height = {}".format(shape.width, shape.height)


class CircleDrawer(ShapeDrawer):
    def draw(self, shape):
        return "Drawing circle with radius = {}".format(shape.radius)


# Client code
rectangle = Rectangle(5, 4)
circle = Circle(5)
rectangle_drawer = RectangleDrawer()
circle_drawer = CircleDrawer()

print(rectangle_drawer.draw(rectangle))
print(circle_drawer.draw(circle))


'''
In the good example, the Shape class is modified to have only one responsibility: calculating the area of the shape. The Rectangle and Circle classes inherit from Shape and override the area method with their own implementation. A new ShapeDrawer class is created to handle the drawing of shapes, which keeps the Shape class closed for modification. The client code can then create instances of the Rectangle and Circle classes and pass them to the ShapeDrawer to draw them without modifying any existing code.
'''
