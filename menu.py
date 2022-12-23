class Menu():

    # def __init__(self, machine):
    #     self.machine = machine

    def print_ingredient_report(self, report):
        for item in report:
            if item != "cash":
                print(f"{item.title()}: {report[item][0]} {report[item][1]}")
            else:
                print(f"Money: ${report[item]}")

    def render_menu(self):
        menu_selections = {
            "R": "Run inventory report",
            "T": "Turn off machine",
        }
        
        print("MENU OPTIONS: ")
        for option in menu_selections:
            print(f"{option}: {menu_selections[option]}")
