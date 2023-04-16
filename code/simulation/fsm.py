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
            print(state, cargo)
            if state == "END":
                return self.base.get_price_paid(), self.base.hs.chosen_coffee.coffee.get_name()
            state, cargo = self.states.handle(state, cargo)
