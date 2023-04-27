'''
Observer is a behavioral design pattern that allows some objects to notify other objects about 
changes in their state.
'''
# Notify all subscriber about the temprature  change
from abc import ABC, abstractmethod

# Observable Interface


class Observable(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setTemp(self, data):
        pass

# Observer Interface


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Implement Observable interface/ abstract class


class WeatherStationObservable(Observable):
    _temp = None
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

    # Whenever temperature gets update notify all the observer
    def setTemp(self, new_temperature):
        if self._temp == new_temperature:
            return
        self._temp = new_temperature
        self.notify()

    def getTemp(self):
        return self._temp


class MobileDisplayObserver(Observer):
    def __init__(self, observable: WeatherStationObservable):
        self.observable = observable

    # Receive observable object and render the data
    def update(self):
        print(
            f"Render the new temperature in Mobile which is {self.observable.getTemp()} degree C")


class TvDisplayObserver(Observer):
    def __init__(self, observable: WeatherStationObservable):
        self.observable = observable

    # Receive observable object and render the data
    def update(self):
        print(
            f"Render the new temperature in TV which is {self.observable.getTemp()} degree C")


# Create the observable
observable = WeatherStationObservable()

# Create the observers and subscribed to observable
observer_1 = MobileDisplayObserver(observable)
observable.add(observer_1)
observer_2 = TvDisplayObserver(observable)
observable.add(observer_2)

# Set the temperature
observable.setTemp(10)
observable.setTemp(10)

# Revome observer
observable.remove(observer_2)

observable.setTemp(12)
