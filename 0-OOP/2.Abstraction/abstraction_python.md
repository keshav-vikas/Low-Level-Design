# Abstraction in Python

## 🔹 What is Abstraction?
Abstraction is one of the core concepts of **Object-Oriented Programming (OOP)**.  

It means **hiding implementation details and showing only the essential features of an object**.  

Think of it like driving a car 🚗:
- You use the steering wheel, brake, and accelerator.  
- But you don’t need to know **how the engine, gearbox, or fuel injection works internally**.  

That’s abstraction: **exposing only what’s necessary and hiding the complexity**.

---

## 🔹 Why Abstraction?
- **Simplifies complexity** → User doesn’t need to worry about inner details.  
- **Improves security** → Hides sensitive code implementation.  
- **Flexibility** → Implementation can change without affecting users.  
- **Enforces a contract** → Defines what must be done, but not how.  

---

## 🔹 Abstraction in Python
In Python, abstraction is mainly achieved using **Abstract Base Classes (ABC)** from the `abc` module.

- An abstract class:
  - **Cannot be instantiated** directly.  
  - Can have **abstract methods** (defined but not implemented).  
  - Subclasses **must implement** those abstract methods.  

---

## 🔹 Example: Abstraction in Python
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")

# Usage
v: Vehicle = Car()
v.start_engine()  # ✅ Car engine started
v.stop_engine()   # ✅ Car engine stopped
```

Here:
- `Vehicle` is an **abstract class**.  
- It defines **what methods must exist** (`start_engine`, `stop_engine`).  
- Subclasses (`Car`, `Bike`) **implement the details**.  

---

## 🔹 Encapsulation vs Abstraction (Quick Difference)
- **Encapsulation** → Hides the internal state/data of an object (using access modifiers).  
- **Abstraction** → Hides implementation details, exposes only essential methods/features.  

---

## ✅ Summary
Abstraction in Python = **hiding implementation details** + **exposing only essential functionality**.  
It’s implemented using **abstract classes and abstract methods** with the `abc` module.  
