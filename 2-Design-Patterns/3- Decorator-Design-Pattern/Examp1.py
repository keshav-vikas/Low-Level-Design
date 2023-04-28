'''
Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing
 them inside special wrapper objects, called decorators.

Decorator is a structural design pattern that lets you attach new behaviors to objects by placing 
these objects inside special wrapper objects that contain the behaviors.

'''

from abc import ABC, abstractmethod


# abstract class
class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass


# child class of BasePizza
class Margherita(BasePizza):
    def cost(self):
        return 100


# child class of BasePizza
class Farmhouse(BasePizza):
    def cost(self):
        return 200


# child class of BasePizza
class VegDelight(BasePizza):
    def cost(self):
        return 150


# abstract class for topping
class ToppingDecorator(BasePizza):
    # it has both the relationship {has-a and is-a relationship } with base pizza class
    # def __init__(self, pizza: BasePizza):
    #     self.pizza = pizza

    @abstractmethod
    def cost(self):
        pass


class ExtraCheese(ToppingDecorator):
    def __init__(self, basePizza):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + 10


class Mushroom(ToppingDecorator):
    def __init__(self, basePizza):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + 20


# Example usage
if __name__ == '__main__':
    # Create a Margherita pizza with extra cheese and mushrooms
    pizza_1 = Mushroom(ExtraCheese(Margherita()))

    # Create a VegDelight pizza with extra cheese and mushrooms
    pizza_2 = Mushroom(ExtraCheese(VegDelight()))

    # Print the cost of each pizza
    print(f"Cost of pizza_1: {pizza_1.cost()}")
    print(f"Cost of pizza_2: {pizza_2.cost()}")
