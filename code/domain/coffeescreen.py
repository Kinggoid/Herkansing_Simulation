class Coffeescreen:
    def __init__(self, hs, coffee):
        self.hs = hs
        self.coffee = coffee

    def pay_coffee(self):
        to_pay = self.coffee.get_price()
        difference = self.hs.coffeemachine.get_price_paid() - to_pay
        if difference >= 0:
            self.hs.coffeemachine.new_balance(to_pay)
            return True
        return False

    def __repr__(self):
        return f"Coffeescreen(coffee='{self.coffee.get_name()}', price='{self.coffee.get_price()}', paid='{self.hs.get_price_paid()})"

