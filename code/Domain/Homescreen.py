from .Coffee import Coffee
from .Coffeescreen import Coffeescreen


class Homescreen:
    _price_paid = 0


    def __init__(self, coffees):
        self._coffees = coffees

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self._price_paid += money

    def get_price_paid(self):
        return self._price_paid

