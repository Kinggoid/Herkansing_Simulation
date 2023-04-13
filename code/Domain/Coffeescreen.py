
class Coffeescreen:

    def __init__(self, hs, coffee):
        self._hs = hs

        self._coffee = coffee

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self._hs.pay_cash(money)

    def make_coffee(self):
        if self._hs.get_price_paid() >= self._coffee.get_price():
            return True
        return False



