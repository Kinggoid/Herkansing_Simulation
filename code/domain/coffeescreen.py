class Coffeescreen:

    def __init__(self, hs, coffee):
        self.hs = hs
        self.coffee = coffee

    def pay_coffee(self):
        difference = self.hs.get_price_paid() - self.coffee.get_price()
        if difference >= 0:
            self.hs.new_balance(difference)
            return True
        return False

    def choose_different_coffee(self):
        return self.hs

    def __repr__(self):
        return f"Coffeescreen(coffee='{self.coffee.get_name()}', price='{self.coffee.get_price()}', paid='{self.hs.get_price_paid()})"

