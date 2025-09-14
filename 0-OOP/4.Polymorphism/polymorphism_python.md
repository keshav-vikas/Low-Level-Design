# Polymorphism in Python

## 🔹 What is Polymorphism?

The word Polymorphism means “many forms”.  
In Object-Oriented Programming (OOP), polymorphism allows the same function or method name to behave differently based on the object or context.

👉 It increases flexibility and reusability.

---

## 🔹 Why Polymorphism?

- **Code Reusability** → One interface, multiple implementations.
- **Flexibility** → Works with different object types seamlessly.
- **Simplifies code** → Same operation works on different classes.
- **Supports Extensibility** → Easy to add new types.

---

## 🔹 Types of Polymorphism in Python

---

### ✅ Polymorphism with Functions and Objects

A function can take different types of objects and call the same method.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
```

Here, animal_sound() works with both Dog and Cat.

---

## ✅ Polymorphism with Inheritance (Method Overriding)

Child class provides a different implementation of a method already defined in parent class.

```python
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Usage
b = Bird()
s = Sparrow()
p = Penguin()

b.fly()  # Some birds can fly
s.fly()  # Sparrow flies high
p.fly()  # Penguins cannot fly


```

## ✅ Polymorphism with Functions/Operators (Overloading-like behavior)

Python does not support traditional function/method overloading like Java or C++.
But, we can achieve similar behavior using default arguments or \*args.

```python
class MathOps:
    def add(self, a, b=0, c=0):
        return a + b + c

m = MathOps()
print(m.add(2))        # 2
print(m.add(2, 3))     # 5
print(m.add(2, 3, 4))  # 9

```

## ✅ Operator Overloading

In Python, operators can be overloaded to work with user-defined classes by defining special methods like **add**, **sub**, etc.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # (4, 6)

```

## 🔹 Summary

- Polymorphism = Same method/operator behaving differently based on context.
- Achieved by:
- Functions working with different objects.
- Method overriding in inheritance.
- Function arguments (\*args, defaults).
- Operator overloading with special methods (**add**, etc.).
