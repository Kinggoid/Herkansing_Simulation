class Coffee:
    cafeine = None
    sugar = None
    price = None

    def __init__(self, coffee):
        self.name = coffee.upper()

    def add_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def coffee_strength_and_sugar_levels(self, cafeine, sugar):
        self.cafeine = cafeine
        self.sugar = sugar

    def __repr__(self):
        return f"Coffee(name='{self.name}', price='{self.price}', cafeine_strength='{self.cafeine}', sugar_strength='{self.sugar}'"
