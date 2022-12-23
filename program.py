class Program():

    def __init__(self, machine, menu):
        self.machine = machine
        self.menu = menu

    def get_selection(self):

        selection = input("SELECTION:").upper()
        return selection

    def execute_selection(self, action):

        actions = {
            "R": (self.menu.print_ingredient_report, self.machine.get_ingredient_report),
            "T": (self.machine.turn_off, None),
        }
        
        self._break_line()
        func, arg = actions[action]
        if arg:
            func(arg())
        else:
            func()
        input("Press Enter...")

    def _break_line(self):
        print("====================")
