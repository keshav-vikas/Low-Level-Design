# https://levelup.gitconnected.com/design-patterns-in-python-strategy-pattern-2189c540756d

'''
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them
 into a separate class, and make their objects interchangeable.
Strategy Pattern is a design pattern that enables our application to select algorithms at runtime,
 making our application flexible.

'''
from abc import ABC, abstractmethod


class SellStrategy(ABC):
    """ it sells BTC and buys USDT """
    @abstractmethod
    def sell_crypto(self, balance: float, currency: float) -> dict:
        """sells crypto and returns new balance"""


class SellAll(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        """critical!! Market doesn't look nice. Sell!"""
        btc = 0
        usdt = balance * currency
        return {"btc": btc, "usdt": usdt}


class SellHalf(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        """ cautious! let's sell half and wait! """
        btc = balance / 2
        usdt = (balance / 2) * currency
        return {"btc": btc, "usdt": usdt}


class SellLittle(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        """ HODL! """
        btc = balance * 0.9
        usdt = (balance * 0.1) * currency
        return {"btc": btc, "usdt": usdt}


class TradingApp:

    assets = {"btc": 100, "usdt": 0}
    currency = 30000

    def sell_order(self, sell_decision: SellStrategy):
        self.assets = sell_decision.sell_crypto(
            self.assets["btc"], self.currency)
        return self.assets


A = TradingApp()
assets = A.sell_order(SellLittle())
print(assets)
#Out: {'btc': 90.0, 'usdt': 300000.0}
assets = A.sell_order(SellHalf())
print(assets)
#Out: {'btc': 45.0, 'usdt': 1350000.0}
