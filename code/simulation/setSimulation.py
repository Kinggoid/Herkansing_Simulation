from code import domain


class StatesHandler:
    def __init__(self, machine, user):
        self.machine = machine
        self.user = user

    def handler(self, state, cargo):
        """Correctly assigns the state to the specific state handler."""
        if state == "q0":
            return self.q0(cargo[0], cargo[1:])
        elif state == "q1":
            return self.q1(cargo[0], cargo[1:])
        elif state == "q2":
            return self.q2(cargo[0], cargo[1:])
        elif state == "q3":
            return self.q3(cargo)
        elif state == "q4":
            return self.q4(cargo)
        elif state == "q5":
            return self.q5(cargo[0], cargo[1:])

    def q0(self, command, cargo):
        if command == "TURN_ON":
            self.machine.turn_on()
            return ["q1", cargo]
        else:
            raise Exception("First turn the coffeemachine on.")

    def q1(self, command, cargo):
        if command == "PAY":
            money = cargo[0]
            try:
                money = float(money)
            except:
                raise Exception("This command: '" + money + "' doesn't correctly specify the amount of money.")
            if self.user.lose_cash(money):
                self.machine.pay_cash(money)
                return ["q1", cargo[1:]]
            raise Exception("User doesn't have enough money to pay this amount.")
        elif command == "CHANGE":
            self.user.gain_cash(self.machine.pay_back_change())
            return "q1", cargo
        elif command == "CHOOSE_COFFEE":
            coffee = cargo[0]
            self.machine.hs.choose_coffee(coffee)
            return "q2", cargo[1:]
        else:
            raise Exception("This command doesn't work.")

    def q2(self, command, cargo):
        if command == "PAY":
            money = cargo[0]
            try:
                money = float(money)
            except:
                raise Exception("This command: '" + money + "' doesn't correctly specify the amount of money.")
            if self.user.lose_cash(money):
                self.machine.pay_cash(money)
                return ["q2", cargo[1:]]
            raise Exception("User doesn't have enough money to pay this amount.")
        elif command == "CHANGE":
            self.user.gain_cash(self.machine.pay_back_change())
            return "q2", cargo
        elif command == "CHOOSE_DIFFERENT_COFFEE":
            self.machine.hs.unchoose_coffee()
            return "q1", cargo
        elif command == "BUY":
            return "q3", cargo
        else:
            raise Exception("This command doesn't work.")

    def q3(self, cargo):
        if self.machine.hs.chosen_coffee.pay_coffee():
            return "q4", cargo
        else:
            return "q2", cargo

    def q4(self, cargo):
        chosen_coffee_name = self.machine.hs.chosen_coffee.coffee.get_name()
        made_coffee = self.machine.make_coffee(chosen_coffee_name)
        self.user.gain_coffee(made_coffee)
        self.machine.hs.unchoose_coffee()
        return "q5", cargo

    def q5(self, command, cargo):
        if command == "CHANGE":
            self.user.gain_cash(self.machine.pay_back_change())
            return "q5", cargo
        elif command == "STOP":
            return "END", None
        else:
            raise Exception("This command doesn't work.")
