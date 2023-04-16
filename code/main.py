import domain
import simulation
from simulation.setSimulation import StatesHandler


def main():
    # Coffees and prices
    coffees = ["Cappuchino", "Espresso", "Latte", "Black"]
    prices = [4, 3, 2, 1]

    # Example user
    user = domain.Person("Kuno", 5)

    # Create coffeemachine
    cm = domain.Coffeemachine(coffees, prices)

    # Couple user and machine
    handler = StatesHandler(cm, user)

    # Initialize simulation
    fsm = simulation.StateMachine(cm, handler)

    # Example FSM simulation command
    cargo = "TURN_ON.CHOOSE_COFFEE.CAPPUCHINO.PAY.0.CHOOSE_DIFFERENT_COFFEE.CHOOSE_COFFEE.BLACK.BUY.PAY.5.BUY.CHANGE.STOP"

    # Run simulation
    fsm.run(cargo)

    # Show results
    print(user)


main()

