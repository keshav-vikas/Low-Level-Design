from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass


class Addition(OperationStrategy):
    def execute(self, num1, num2):
        return num1 + num2


class Subtraction(OperationStrategy):
    def execute(self, num1, num2):
        return num1 - num2


class Multiplication(OperationStrategy):
    def execute(self, num1, num2):
        return num1 * num2


class Division(OperationStrategy):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("division by zero")
        return num1 / num2


class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, num1, num2):
        return self.strategy.execute(num1, num2)


add = Calculator(Addition())
result = add.calculate(5, 3)
print(result)

sub = Calculator(Subtraction())
result = sub.calculate(5, 3)
print(result)  # Output: 2


mul = Calculator(Multiplication())
result = mul.calculate(5, 3)
print(result)

div = Calculator(Division())
result = div.calculate(5, 3)
print(result)
