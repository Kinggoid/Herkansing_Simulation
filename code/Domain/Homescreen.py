class Homescreen:
    def __init__(self, coffees, prices):
        self.coffees = coffees
        self.prices = prices

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self.paid = money

    def select_coffee(self):
        while True:

            break