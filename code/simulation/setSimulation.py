from code import domain


def q1(state, command, cargo):
    if command == "PAY":
        money = cargo[1]
        state.pay_cash(money)

        return state, cargo[2:]

    elif command == "CHANGE":
        state.pay_back_change()
        return state, cargo[1:]

    elif command == "CHOOSE_COFFEE":
        coffee = cargo[1]
        return state.coffees[coffee], cargo[2:]


def q2(state, command, cargo):
    if command == "PAY":
        money = cargo[1]
        state.pay_cash(money)
        return state, cargo[2:]

    elif command == "CHOOSE_DIFFERENT_COFFEE":
        return state.choose_different_coffee, cargo[1:]

    elif command == "BUY":
        coffee = cargo[1]
        bought_coffee = state.pay_coffee()
        if bought_coffee:
            return state.coffees[coffee], cargo[2:]
        else:
            return state, cargo[2:]


def q3(state, command, cargo):
    if command == "CHOOSE_DIFFERENT_COFFEE":
        return state.choose_different_coffee, cargo[1:]

    elif command == "BUY":
        coffee = cargo[1]
        bought_coffee = state.pay_coffee()
        if bought_coffee:
            return state.coffees[coffee], cargo[2:]
        else:
            return state, cargo[2:]


