# Inheritance in Python

## 🔹 What is Inheritance?
**Inheritance** is an **Object-Oriented Programming (OOP)** concept where a class (called the **child** or **derived class**) can **reuse properties and methods** from another class (called the **parent** or **base class**).  

It allows **code reusability** and helps in building hierarchical relationships between classes.  

---

## 🔹 Why Inheritance?
- **Code Reusability** → Child classes reuse parent code without rewriting it.  
- **Extensibility** → Existing classes can be extended with new features.  
- **Hierarchy Representation** → Models "is-a" relationships.  
- **Polymorphism Support** → Same method name can behave differently in different classes.  

---

## 🔹 Types of Inheritance in Python
1. **Single Inheritance** – One parent, one child.  
2. **Multiple Inheritance** – Child inherits from more than one parent.  
3. **Multilevel Inheritance** – A chain of inheritance (grandparent → parent → child).  
4. **Hierarchical Inheritance** – Multiple child classes inherit from the same parent.  
5. **Hybrid Inheritance** – Combination of the above types.  

---

## 🔹 Example 1: Single Inheritance
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Usage
a = Animal()
a.speak()   # Animal makes a sound

d = Dog()
d.speak()   # Dog barks
```

Here, `Dog` inherits from `Animal` and overrides the `speak()` method.  

---

## 🔹 Example 2: Multiple Inheritance
```python
class Father:
    def skill(self):
        print("Father: Gardening")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill(self):
        print("Child: Coding")

# Usage
c = Child()
c.skill()  # Child: Coding
```

Here, `Child` inherits from both `Father` and `Mother`.  
If not overridden, Python follows **Method Resolution Order (MRO)** to decide which parent’s method to call.  

---

## 🔹 Example 3: Multilevel Inheritance
```python
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()  # Hello from Parent
```

Here, `Child` indirectly inherits from `Grandparent` through `Parent`.  

---

## 🔹 Example 4: Hierarchical Inheritance
```python
class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def drive(self):
        print("Driving car")

class Bike(Vehicle):
    def ride(self):
        print("Riding bike")

c = Car()
c.start()  # Starting vehicle...
c.drive()  # Driving car

b = Bike()
b.start()  # Starting vehicle...
b.ride()   # Riding bike
```

---

## 🔹 Example 5: Using `super()` in Inheritance
`super()` is used to call methods from the parent class.  

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # call parent constructor
        self.emp_id = emp_id

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

e = Employee("Alice", 101)
e.display()  # Name: Alice, ID: 101
```

---

## ✅ Summary
- **Inheritance** allows one class to **reuse and extend** another class.  
- Python supports:
  - Single
  - Multiple
  - Multilevel
  - Hierarchical
  - Hybrid inheritance  
- Use **`super()`** to call parent class methods/constructors.  
