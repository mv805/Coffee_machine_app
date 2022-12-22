import coffee_machine

machine = coffee_machine.CoffeeMachine()


def print_ingredient_report(machine):
    report = machine.get_ingredient_report()
    for item in report:
        if item != "cash":
            print(f"{item.title()}: {report[item][0]} {report[item][1]}")
        else:
            print(f"Money: ${report[item]}")

print_ingredient_report(machine)