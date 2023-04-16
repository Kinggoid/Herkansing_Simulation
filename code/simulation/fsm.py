from .state import State
from code import domain
from .setSimulation import StatesHandler


class InitializationError(Exception):
    pass


class StateMachine:
    def __init__(self, base, states):
        self.base = base
        self.states = states

    def run(self, cargo):
        cargo = cargo.split(".")
        state = "q0"

        while True:
            print(cargo[0])
            state, cargo = self.states.handle(state, cargo)
            if state == "END":
                return self.base.get_price_paid(), self.base.hs.chosen_coffee.get_name

