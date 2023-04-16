import domain
import simulation
from simulation.setSimulation import StatesHandler

harry = domain.Person("Harry", 5)
coffees = ["Cappuchino", "Espresso", "Latte", "Black"]
prices = [4,3,2,1]

cm = domain.Coffeemachine(coffees, prices)
handler = StatesHandler(cm, harry)

# q0 = simulation.State("q0", setsim.q1, startstate=1)
# q1 = simulation.State("q1", setsim.q2, endstate=1)
# q2 = simulation.State("q2")
# q3 = simulation.State("q3")
# q4 = simulation.State("q4")
# q5 = simulation.State("q5", endstate=1)


# fsm = simulation.StateMachine([q0, q1])

fsm = simulation.StateMachine(cm, handler)

cargo = "TURN_ON.PAY.20.END"
fsm.run(cargo)



# cff = coffees_in_machine[0]
# q1.choose_option(0, 20, cff)


