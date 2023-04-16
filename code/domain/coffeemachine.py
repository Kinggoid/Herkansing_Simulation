from .coffee import Coffee
from .coffeescreen import Coffeescreen
from .homescreen import Homescreen


class Coffeemachine:
    price_paid = 0
    coffees = []
    prices = []
    turned_on = False

    def __init__(self, coffees, prices):
        self.hs = Homescreen(self)

        for i in range(len(coffees)):
            self.coffees.append(Coffeescreen(self.hs, Coffee(coffees[i], prices[i])))

        self.prices = prices
        self.hs.add_coffees(self.coffees)

    def turn_on(self):
        self.turned_on = True

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self.price_paid += money

    def new_balance(self, money):
        self.price_paid -= money

    def get_price_paid(self):
        return self.price_paid

    def pay_back_change(self):
        change = self.price_paid
        self.price_paid = 0
        return change

    def make_coffee(self, coffee_name):
        return coffee_name

    def __repr__(self):
        return f"Homescreen(price_paid='{self.price_paid}')"