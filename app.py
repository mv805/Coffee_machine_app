import coffee_machine
from menu import Menu
from os import system

def clear():
    _ = system('cls')


machine = coffee_machine.CoffeeMachine()
menu = Menu(machine)


while machine.is_on:
    clear()
    menu.render_menu()
    selection = menu.get_selection()
    menu.execute_action(selection)


