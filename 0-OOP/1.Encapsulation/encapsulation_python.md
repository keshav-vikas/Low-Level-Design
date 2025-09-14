# Encapsulation in Python

## 🔹 What is Encapsulation?

Encapsulation is one of the core concepts of **Object-Oriented Programming (OOP)**.  
It means **bundling data (variables/attributes) and methods (functions) that operate on that data into a single unit (class)**, and restricting direct access to some parts of the object.

Think of it like a **capsule**: it keeps data and methods inside, and only exposes what’s necessary.

---

## 🔹 Why Encapsulation?

- **Data Hiding** → Prevents direct modification of variables from outside the class.
- **Controlled Access** → Provides controlled ways (via getters and setters) to read or modify data.
- **Security** → Keeps the object’s internal state safe.
- **Flexibility** → Internal implementation can change without affecting external code.

---

## 🔹 Encapsulation in Python

In Python, encapsulation is achieved using **access modifiers** (by naming conventions):

### 1. Public Members

Accessible from anywhere.  
No underscore prefix.

```python
class Student:
    def __init__(self, name):
        self.name = name  # public

s = Student("Alice")
print(s.name)  # ✅ accessible
```

---

### 2. Protected Members

By convention, marked with a **single underscore `_`**.  
Should not be accessed directly outside the class, but still possible.

```python
class Student:
    def __init__(self, name, age):
        self._age = age  # protected

s = Student("Alice", 20)
print(s._age)  # ⚠️ possible, but discouraged
```

---

### 3. Private Members

Marked with **double underscore `__`**.  
Cannot be accessed directly from outside (name mangling happens).

```python
class Student:
    def __init__(self, name, age):
        self.__age = age  # private

    def get_age(self):
        return self.__age  # controlled access

s = Student("Alice", 20)
# print(s.__age)  # ❌ AttributeError
print(s.get_age())  # ✅ controlled access
```

---

## 🔹 Example: Full Encapsulation

```python
class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # private

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # ✅ 1300
```

Here:

- `__balance` is **hidden** from direct access.
- Access is only via `deposit`, `withdraw`, and `get_balance`.

---

## ✅ Summary

Encapsulation in Python = **binding data + methods inside a class** + **controlling access (public, protected, private)**.  
It protects the internal state and ensures controlled modification.
