from .coffee import Coffee
from .coffeescreen import Coffeescreen
from .homescreen import Homescreen


class Coffeemachine:
    price_paid = 0
    turned_on = False

    def __init__(self, coffees, prices):
        self.hs = Homescreen(self)

        coffee_screens = []
        for i in range(len(coffees)):
            coffee_screens.append(Coffeescreen(self.hs, Coffee(coffees[i], prices[i])))
        self.hs.add_coffees(coffee_screens)

    def turn_on(self):
        self.turned_on = True

    def pay_cash(self, money):
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
        return f"Coffeemachine(price_paid='{self.price_paid}', coffees='{self.coffees}', prices='{self.prices}', turned_on='{self.turned_on}')"
