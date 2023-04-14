class Coffeescreen:

    def __init__(self, hs, coffee):
        self._hs = hs
        self._coffee = coffee

    def pay_cash(self, money):
        """Pay your coffee in cash"""
        self._hs.pay_cash(money)

    def get_price_paid(self):
        return self._hs.get_price_paid()

    def make_coffee(self):
        if self._hs.get_price_paid() >= self._coffee.get_price():
            return True
        return False

    def __repr__(self):
        return f"Coffeescreen(coffee='{self._coffee.get_name()}', price='{self._coffee.get_price()}', paid='{self._hs.get_price_paid()})"

