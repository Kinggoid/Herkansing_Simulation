import domain
import simulation
from simulation.setSimulation import StatesHandler

harry = domain.Person("Harry", 20)
coffees = ["Cappuchino", "Espresso", "Latte", "Black"]
prices = [4, 3, 2, 1]

cm = domain.Coffeemachine(coffees, prices)
handler = StatesHandler(cm, harry)

fsm = simulation.StateMachine(cm, handler)

cargo = "TURN_ON.PAY.10.CHANGE.PAY.5.CHOOSE_COFFEE.CAPPUCHINO.PAY.5.CHOOSE_DIFFERENT_COFFEE.CHOOSE_COFFEE.BLACK.BUY.CHANGE.STOP"
fsm.run(cargo)



# cff = coffees_in_machine[0]
# q1.choose_option(0, 20, cff)


