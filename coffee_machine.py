from ingredient import Ingredient


class CoffeeMachine():

    ingredients = {
        "water": (Ingredient("water", "ml"), 2500),
        "milk": (Ingredient("milk", "ml"), 1000),
        "coffee": (Ingredient("coffee", "g"), 500),
        "honey": (Ingredient("honey", "oz"), 50),
    }

    drinks = {
        "espresso": {
            "price": 2.50,
            "ingredients": [("water", 10), ("milk", 30), ("coffee", 50)]
        },
        "latte": {
            "price": 1.00,
            "ingredients": [("water", 30), ("milk", 40), ("coffee", 10)]
        },
        "cappuccino": {
            "price": 1.50,
            "ingredients": [("water", 10), ("milk", 50), ("coffee", 100)]
        },
    }

    _machine_is_on = False
    _cash = 0

    def __init__(self):
        self.turn_on()

    def _get_remaining_of_ingredient(self, ingredient):
        ingredient_to_check, quantity_remaining = self.ingredients[ingredient]
        return quantity_remaining

    def get_ingredient_report(self):
        report = {}
        for ingredient in self.ingredients:  # iterates through the keys
            report[ingredient] = (
                self.ingredients[ingredient][1], self.ingredients[ingredient][0].get_uom())

        report["cash"] = self._cash
        return report

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
        return power_status
