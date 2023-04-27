# low-level design Python code for notifying all users who have asked to be notified when items come into stock:

from abc import ABC, abstractmethod

# Observable Interface


class StockObservable(ABC):
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setStockCount(self, newCount):
        pass

    @abstractmethod
    def getStockCount(self):
        pass


class IphoneObservable(StockObservable):
    _stockCount = 0
    _observers = []

    # Add an observer
    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)

    def notify(self):
        # Notify all the observers
        for observer in self._observers:
            observer.update()

    # Whenever stock gets update notify all the observer
    def setStockCount(self, newCount):
        if self._stockCount == 0:
            self.notify()
        self._stockCount += newCount

    def getStockCount(self):
        return self._stockCount

# Observer Interface


class NotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, email, observable: IphoneObservable):
        self.observable = observable
        self.email = email

    # Receive observable object and send mail
    def update(self):
        print("Mail sent to ", self.email)


class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, userName, observable: IphoneObservable):
        self.observable = observable
        self.userName = userName

    # Receive observable object and send msg
    def update(self):
        print("Message sent to ", self.userName)


if __name__ == "__main__":
    iphonStockObservable = IphoneObservable()

    observer1 = EmailAlertObserver('keshav@email.com', iphonStockObservable)
    observer2 = EmailAlertObserver('vikas@email.com', iphonStockObservable)
    observer3 = MobileAlertObserver('Keshav', iphonStockObservable)

    iphonStockObservable.add(observer1)
    iphonStockObservable.add(observer2)
    iphonStockObservable.add(observer3)

    iphonStockObservable.setStockCount(11)
    iphonStockObservable.setStockCount(0)
    iphonStockObservable.setStockCount(11)
