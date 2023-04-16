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
            coffee = Coffee(coffees[i])
            coffee.add_price(prices[i])
            coffee_screens.append(Coffeescreen(self.hs, coffee))
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

    def make_coffee(self, coffee_name, cafeine, sugar):
        new_coffee = Coffee(coffee_name)
        new_coffee.coffee_strength_and_sugar_levels(cafeine, sugar)
        return new_coffee

    def __repr__(self):
        return f"Coffeemachine(price_paid='{self.price_paid}', turned_on='{self.turned_on}')"
