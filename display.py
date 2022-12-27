class Display():

    def print_ingredient_report(self, report):
        for item in report:
            if item != "cash":
                print(f"{item.title()}: {report[item][0]} {report[item][1]}")
            else:
                print(f"Money: ${report[item]: .2f}")

    def render_selection_menu(self):
        menu_selections = {
            "R": "Run inventory report",
            "T": "Turn off machine",
            "D": "Make a drink",
        }

        print("MENU OPTIONS: ")
        for option in menu_selections:
            print(f"{option}: {menu_selections[option]}")

    def render_drink_menu(self, drink_list):
        """renders a menu that displays all available drinks"""

        for index, (drink, data) in enumerate(drink_list.items()):
            print(f"{index + 1}: {drink.title()}, ${data['price']: .2f}")
