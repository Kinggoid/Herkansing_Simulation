class Coffee:
    made = 0

    def __init__(self, coffee, price):
        self._name = coffee
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, coffee):
        self._name = coffee

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def __repr__(self):
        return f"Coffee(name='{self._name}', price='{self._price}')"
