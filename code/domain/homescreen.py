from .coffee import Coffee
from .coffeescreen import Coffeescreen
from .coffeemachine import Coffeemachine


class Homescreen:
    coffeescreens = {}

    def __init__(self, machine):
        self.coffeemachine = machine

    def add_coffees(self, coffeescreens):
        for coffeescreen in coffeescreens:
            self.coffeescreens[coffeescreen.coffee.get_name()] = coffeescreen

    def remove_coffee(self, coffee):
        self.coffeescreens.pop(coffee)

    def choose_coffee(self, coffee):
        return self.coffeescreens[coffee]
