class Person:
    def __init__(self, name, pocket_change):
        self.name = name
        self.pocket_change = pocket_change

    def pay_cash(self, money):
        if self.pocket_change >= money:
            self.pocket_change -= money
            return True
        else:
            return False

    def gain_cash(self, money):
        self.pocket_change += money
