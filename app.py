import coffee_machine
from menu import Menu
from program import Program
from os import system


def clear():
    _ = system('cls')


machine = coffee_machine.CoffeeMachine()
menu = Menu()
program = Program(machine, menu)


while machine.is_on:
    clear()
    menu.render_menu()
    selection = program.get_selection()
    program.execute_selection(selection)
