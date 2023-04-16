class Coffeescreen:
    strength_levels = ["LOW", "MEDIUM", "HIGH"]
    cafeine = "LOW"
    sugar = "LOW"

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

    def change_cafeine_level(self, strength):
        if strength in self.strength_levels:
            self.cafeine = strength
        else:
            raise Exception("Strength not in strength levels.")

    def change_sugar_level(self, strength):
        if strength in self.strength_levels:
            self.sugar = strength
        else:
            raise Exception("Strength not in strength levels.")

    def __repr__(self):
        return f"Coffeescreen(coffee='{self.coffee.get_name()}', price='{self.coffee.get_price()}')"

