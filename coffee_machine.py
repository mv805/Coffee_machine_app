from coffee_machine_app.ingredient import Ingredient

class CoffeeMachine():

    ingredients = {
        "milk": (Ingredient("milk", "ml"), 1000),
        "water": (Ingredient("water", "ml"), 2500),
        "water": (Ingredient("coffee", "g"), 500),
    }

    _machine_is_on = False

    def __init__(self):
        self.turn_on()

    def _get_remaining_of_ingredient(self, ingredient):
        ingredient_to_check, quantity_remaining = self.ingredients[ingredient]
        return f"The machine has Qty:{quantity_remaining} {ingredient_to_check.get_uom()} of {ingredient_to_check.get_name().title()} left."

    def turn_on(self):
        print("The coffee machine is turning on...")
        self._machine_is_on = True

    def turn_off(self):
        print("The coffee machine is turning off...")
        self._machine_is_on = False

    def get_power_status(self):
        if self._machine_is_on:
            power_status = "on"
        else:
            power_status = "off"
        print(f"The machine is currently turned {power_status}")
