class StateMachine:
    def __init__(self, base, states):
        self.base = base
        self.states = states

    def run(self, cargo):
        cargo = cargo.split(".")
        state = "q0"

        while True:
            if state == "END":
                break
            state, cargo = self.states.handler(state, cargo)
