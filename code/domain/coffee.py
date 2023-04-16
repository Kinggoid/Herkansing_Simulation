class Coffee:
    made = 0

    def __init__(self, coffee, price):
        self.name = coffee.upper()
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, coffee):
        self.name = coffee

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __repr__(self):
        return f"Coffee(name='{self.name}', price='{self.price}')"
