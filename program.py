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
            "D": (self.request_drink, None),
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
    
    def request_drink(self):

        # drink_menu dict is dynamically filled in the manner below
        # drink_menu = {
        #     1: 'espresso',
        #     2: 'latte',
        #     ...
        # }
        drink_menu = {}
        drink_list = self.machine.get_drink_list()

        print("DRINK MENU:")
        self.menu.render_drink_menu(drink_list)
        for index, (drink, data) in enumerate(drink_list.items()):
            drink_menu[index + 1] = drink
        user_selection = input("Please select a drink:")


