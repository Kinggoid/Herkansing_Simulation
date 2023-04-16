from code import domain


class StatesHandler:
    def __init__(self, machine, user):
        self.machine = machine
        self.person = user

    def handle(self, state, cargo):

        if state == "q0":
            return self.q0(cargo[0], cargo[1:])
        elif state == "q1":
            return self.q1(cargo[0], cargo[1:])
        elif state == "q2":
            return self.q2(cargo[0], cargo[1:])
        elif state == "q3":
            return self.q3(None, cargo)
        elif state == "q4":
            return self.q4(None, cargo)
        elif state == "q5":
            return self.q5(cargo[0], cargo[1:])
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
            coffee = cargo[0]
            self.machine.hs.choose_coffee(coffee)
            return "q2", cargo[1:]
        else:
            raise ValueError("This command doesn't work.")

    def q2(self, command, cargo):
        if command == "PAY":
            money = cargo[0]
            self.machine.pay_cash(money)
            return "q2", cargo[1:]

        elif command == "CHOOSE_DIFFERENT_COFFEE":
            self.machine.hs.unchoose_coffee()
            return "q1", cargo[1:]

        elif command == "BUY":
            return "q3", cargo
        else:
            raise ValueError("This command doesn't work.")

    def q3(self, command, cargo):
        if self.machine.hs.chosen_coffee.pay_coffee():
            return "q4", cargo
        else:
            return "q2", cargo

    def q4(self, command, cargo):
        self.machine.make_coffee(self.machine.hs.chosen_coffee.coffee.get_name())
        return "q5", cargo

    def q5(self, command, cargo):
        if command == "CHANGE":
            self.machine.pay_back_change()
            return "q5", cargo
        elif command == "STOP":
            return "END", None
        else:
            raise ValueError("This command doesn't work.")
