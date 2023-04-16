class Coffee:
    made = 0

    def __init__(self, coffee, price):
        self.name = coffee.upper()
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __repr__(self):
        return f"Coffee(name='{self.name}', price='{self.price}')"
