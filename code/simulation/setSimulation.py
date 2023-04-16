from code import domain


class StatesHandler:
    def __init__(self, machine, user):
        self.machine = machine
        self.person = user

    def handle(self, state, cargo):
        command = cargo[0]
        cargo = cargo[1:]

        if state == "q0":
            return self.q0(command, cargo)
        elif state == "q1":
            return self.q1(command, cargo)
        # elif state == "q2":
        #     return self.q0(command, cargo)
        # elif state == "q3":
        #     return self.q0(command, cargo)
        # elif state == "q4":
        #     return self.q0(command, cargo)
        # elif state == "q5":
        #     return self.q0(command, cargo)
        else:
            raise ValueError("This command doesn't work.")

    def q0(self, command, cargo):
        if command == "TURN_ON":
            self.machine.turn_on()
            return ["q1", cargo]
        else:
            raise ValueError("This command doesn't work.")

    def q1(self, command, cargo):
        if command == "PAY":
            money = cargo[0]

            try:
                money = float(money)
            except:
                raise ValueError("This command: '" + command + "' doesn't correctly specify money")

            self.machine.pay_cash(money)

            return ["q1", cargo[1:]]

        elif command == "CHANGE":
            self.machine.pay_back_change()
            return "q1", cargo

        elif command == "CHOOSE_COFFEE":
            coffee = cargo[1]
            self.machine.hs.choose_coffee(coffee)
            return "q2", cargo[1:]
        else:
            raise ValueError("This command doesn't work.")


    # def q2(state, command, cargo):
    #     if command == "PAY":
    #         money = cargo[1]
    #         state.pay_cash(money)
    #         return state, cargo[2:]
    #
    #     elif command == "CHOOSE_DIFFERENT_COFFEE":
    #         return state.choose_different_coffee, cargo[1:]
    #
    #     elif command == "BUY":
    #         coffee = cargo[1]
    #         bought_coffee = state.pay_coffee()
    #         if bought_coffee:
    #             return state.coffees[coffee], cargo[2:]
    #         else:
    #             return state, cargo[2:]
    #
    #
    # def q3(state, command, cargo):
    #     if command == "CHOOSE_DIFFERENT_COFFEE":
    #         return state.choose_different_coffee, cargo[1:]
    #
    #     elif command == "BUY":
    #         coffee = cargo[1]
    #         bought_coffee = state.pay_coffee()
    #         if bought_coffee:
    #             return state.coffees[coffee], cargo[2:]
    #         else:
    #             return state, cargo[2:]
    #
    #
