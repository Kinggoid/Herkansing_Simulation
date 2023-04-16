class Homescreen:
    coffeescreens = {}
    chosen_coffee = None

    def __init__(self, machine):
        self.coffeemachine = machine

    def add_coffees(self, coffeescreens):
        for coffeescreen in coffeescreens:
            self.coffeescreens[coffeescreen.coffee.get_name()] = coffeescreen

    def remove_coffee(self, coffee):
        self.coffeescreens.pop(coffee)

    def choose_coffee(self, coffee):
        self.chosen_coffee = self.coffeescreens[coffee]

    def unchoose_coffee(self):
        self.chosen_coffee = None
