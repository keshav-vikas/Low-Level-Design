class Circle:
    #define data attributes within the constructor
    def __init__(self, r=0):
        self.radius = r
        self.pi = 3.142

    #define methods
    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius

def main():
    circle = Circle(5)
    print("Area: {:.2f}".format(circle.area()))
    print("Perimeter: {:.2f}".format(circle.perimeter()))

if __name__ == "__main__":
    main()

'''
As you can see, we only need to define the radius of the circle in the constructor. After that, the area() and perimeter() functions are available to us. This interface is part of encapsulation.

We use the functions to calculate the area and perimeter. Users do not need to know the implementation details of the functions. Even pi is hidden since it’s a constant. This is how we can achieve abstraction using classes.
'''