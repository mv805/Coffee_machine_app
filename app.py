import coffee_machine
from display import Display
from program import Program
from os import system


def clear():
    _ = system('cls')


machine = coffee_machine.CoffeeMachine()
display = Display()
program = Program(machine, display)


while machine.is_on:
    clear()
    display.render_selection_menu()
    selection = program.get_selection()
    program.execute_selection(selection)
