'''
Factory Method is a creational design pattern that provides an interface for creating objects in a
 superclass, but allows subclasses to alter the type of objects that will be created.

The Factory Design Pattern is a creational pattern that provides an interface (or a method) for 
creating objects, but allows subclasses (or derived classes) to alter the type of objects that will be created. 

In other words, the Factory Design Pattern allows you to create objects without knowing the exact
 class of object that will be created, by delegating the responsibility of creating objects to a separate factory class. 
 
The benefit of using the Factory Design Pattern is that it allows you to encapsulate the object 
creation process and make your code more modular and flexible. For example, you can add new types of 
objects to the system by simply adding a new subclass and modifying the factory class, without having to modify any other code

ref:
https://levelup.gitconnected.com/design-patterns-in-python-factory-pattern-beea1da31c17
'''

from abc import ABC, abstractmethod

# Abstract class for the Shape


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete classes for different types of shapes


class Circle(Shape):
    def draw(self):
        print("Drawing circle")


class Square(Shape):
    def draw(self):
        print("Drawing Square")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

# Factory class for creating different types of shape


class ShapeFactory:
    def getShape(self, input):

        if input.lower() == "circle":
            return Circle()
        elif input.lower() == "square":
            return Square()
        elif input.lower() == "rectangle":
            return Rectangle()
        else:
            return None


# Example usage
if __name__ == '__main__':
    shapefactoryObj = ShapeFactory()
    shapeObj1 = shapefactoryObj.getShape("circle")
    shapeObj1.draw()
    shapeObj2 = shapefactoryObj.getShape("square")
    shapeObj2.draw()
