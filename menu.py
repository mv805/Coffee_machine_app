class Menu():

    def __init__(self, machine):
        self.machine = machine

    def print_ingredient_report(self):
        report = self.machine.get_ingredient_report()
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
    
    def get_selection(self):
        
        selection = input("SELECTION:").upper()
        return selection
        

    def execute_action(self, action):
        actions = {
            "R": self.print_ingredient_report,
            "T": self.machine.turn_off,
        }
        self._break_line()
        actions[action]()
        input("Press Enter...")
    
    def _break_line(self):
        print("====================")
