from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Item(Subject):
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def update_stock(self, new_stock):
        old_stock = self.stock
        self.stock = new_stock
        if old_stock == 0 and new_stock > 0:
            self.notify_observers()


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class User(Observer):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update(self, subject):
        if subject.stock > 0:
            print(
                f"Notification sent to {self.name} at {self.email}: {subject.name} is back in stock!")
        else:
            print(
                f"Notification sent to {self.name} at {self.email}: {subject.name} is out of stock.")


class Inventory:
    def __init__(self):
        self._items = {}

    def add_item(self, item):
        self._items[item.name] = item

    def remove_item(self, item):
        del self._items[item.name]

    def update_item_stock(self, item_name, new_stock):
        item = self._items.get(item_name)
        if item:
            item.update_stock(new_stock)
        else:
            print(f"Item {item_name} not found in inventory.")

    def register_user(self, item_name, user):
        item = self._items.get(item_name)
        if item:
            item.attach(user)
        else:
            print(f"Item {item_name} not found in inventory.")

    def unregister_user(self, item_name, user):
        item = self._items.get(item_name)
        if item:
            item.detach(user)
        else:
            print(f"Item {item_name} not found in inventory.")


item1 = Item("item1", 0)
item2 = Item("item2", 5)

user1 = User("John", "john@example.com")
user2 = User("Jane", "jane@example.com")

inventory = Inventory()
inventory.add_item(item1)
inventory.add_item(item2)

inventory.update_item_stock("item1", 2)
inventory.update_item_stock("item1", 0)
inventory.update_item_stock("item2", 2)

inventory.register_user("item1", user1)
inventory.register_user("item1", user2)
inventory.register_user("item2", user2)

inventory.update_item_stock("item1", 1)
inventory.update_item_stock("item2", 5)

# inventory.unregister_user("item1", user1)
# inventory.unregister_user("item2", user2)
