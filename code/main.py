import domain
import simulation
import simulation.setSimulation as setsim


coffees = ["Cappuchino", "Espresso", "Latte", "Black"]
prices = [4,3,2,1]

cm = domain.Coffeemachine(coffees, prices)

q0 = simulation.State("q0", setsim.q1, startstate=1)
q1 = simulation.State("q1", setsim.q2, endstate=1)
# q2 = simulation.State("q2")
# q3 = simulation.State("q3")
# q4 = simulation.State("q4")
# q5 = simulation.State("q5", endstate=1)


fsm = simulation.StateMachine([q0, q1])

sim = "PAY.20"
fsm.run(sim, cm)



# cff = coffees_in_machine[0]
# q1.choose_option(0, 20, cff)


