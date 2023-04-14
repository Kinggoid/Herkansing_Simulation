from .coffee import Coffee
from .coffeescreen import Coffeescreen


class Homescreen:
    _price_paid = 0

    def __init__(self, coffees):
        self._coffees = coffees

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self._price_paid += money

    def get_price_paid(self):
        return self._price_paid

    def __repr__(self):
        return f"Homescreen(price_paid='{self._price_paid}')"

