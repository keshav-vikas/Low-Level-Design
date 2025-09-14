'''
 method overriding.

Suppose we have a parent class, Animal, with its subclass, Lion. Below is the implementation of two functions with the same name in each class to check method overriding behavior.
'''
class Animal:
  def __init__(self):
    pass
  
  def print_animal(self):
    print("I am from the Animal class")

  def print_animal_two(self):
    print("I am from the Animal class")


class Lion(Animal):
  
  def print_animal(self): # method overriding
    print("I am from the Lion class")


lion = Lion()
lion.print_animal()
lion.print_animal_two()

'''
Method overloading
'''
class Area:
    def calculateArea(self, length, breadth=-1):
        if breadth != -1:
            return length * breadth;
        else:
            return length * length;


area = Area()
print("Area of rectangle = " + str(area.calculateArea(3, 4)))
print("Area of square = " + str(area.calculateArea(6)))

'''
Operator overloading
'''
class ComplexNumber: 
    # Constructor
    def __init__(self): 
        self.real = 0 
        self.imaginary = 0 
    # Set value function
    def set_value(self, real, imaginary): 
        self.real = real
        self.imaginary = imaginary 
    # Overloading function for + operator
    def __add__(self, c): 
        result = ComplexNumber() 
        result.real = self.real + c.real 
        result.imaginary = self.imaginary + c.imaginary 
        return result 
    # display results
    def display(self): 
        print( "(", self.real, "+", self.imaginary, "i)") 
 
 
c1 = ComplexNumber() 
c1.set_value(11, 5) 
c2 = ComplexNumber() 
c2.set_value(2, 6) 
c3 = c1 + c2
c3.display() 