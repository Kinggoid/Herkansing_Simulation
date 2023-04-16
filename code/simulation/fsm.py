from .state import State
from code import domain


class InitializationError(Exception):
    pass


class StateMachine:
    states = []
    options = {}
    startState = None
    endStates = []

    def __init__(self, states):
        for state in states:
            if state.startstate:
                self.startState = state
            elif state.endstate:
                self.endStates.append(state)
            self.states.append(states)

    def run(self, cargo, hs):
        # try:
        #     handler = self.handlers[self.startState]
        # except:
        #     raise InitializationError("Must call .set_start() before .run()")
        # if not self.endStates:
        #     raise InitializationError("Must call .set_() beendfore .run(). At least one state must be an end_state")
        state = hs

        cargo = cargo.split(".", 1)

        while True:
            print(cargo)
            state = state.execute(state, cargo[0], cargo)
            print(hs.get_price_paid())

            cargo.pop(0)

