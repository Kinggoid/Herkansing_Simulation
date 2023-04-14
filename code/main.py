import domain

coffees = ["Cappuchino", "Espresso", "Latte", "Black"]
prices = [4,3,2,1]

hs = domain.Homescreen(coffees)

coffees_in_machine = []

for i in range(len(coffees)):
    coffees_in_machine.append(domain.Coffeescreen(hs, domain.Coffee(coffees[i], prices[i])))

while True:
    print("These are the coffees that are currently available: ")
    for i in range(0, len(coffees_in_machine)):
        print(str(i + 1) + ": " + coffees[i])

    chosen_coffee_number = eval(input("\nType in the number of the coffee you want: "))

    try:
        correct_chosen_coffee_number = int(chosen_coffee_number) - 1
    except:
        print("\nError: not an available option. Try again.\n")
        continue

    if 0 > correct_chosen_coffee_number or correct_chosen_coffee_number >= len(coffees):
        print("\nError: not an available option. Try again.\n")
        continue
    break

chosen_coffee = coffees_in_machine[correct_chosen_coffee_number]
chosen_coffee.pay_cash(10)
print(chosen_coffee.make_coffee())

