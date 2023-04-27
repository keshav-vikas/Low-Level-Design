# low-level design Python code for notifying all users who have asked to be notified when items come into stock:
class Item:
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
        if old_stock == 0 and new_stock > 0:
            self.notify_observers()
        #self.stock = new_stock + old_stock
        self.stock = new_stock


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update(self, item):
        print(f"Dear {self.name}, the item {item.name} is now in stock.")


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def get_item(self, name):
        return self.items.get(name)

    def update_item_stock(self, name, new_stock):
        item = self.get_item(name)
        if item:
            item.update_stock(new_stock)


if __name__ == "__main__":
    inventory = Inventory()

    # add items to inventory
    item1 = Item("item1", 0)
    item2 = Item("item2", 0)
    inventory.add_item(item1)
    inventory.add_item(item2)

    # create users and attach them to items
    user1 = User("user1", "user1@example.com")
    user2 = User("user2", "user2@example.com")
    item1.attach(user1)
    item2.attach(user1)
    item2.attach(user2)

    # update item stocks
    inventory.update_item_stock("item1", 1)
    inventory.update_item_stock("item5", 2)
    inventory.update_item_stock("item2", 3)
    inventory.update_item_stock("item1", 0)
    inventory.update_item_stock("item1", 5)
