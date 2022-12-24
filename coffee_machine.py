from ingredient import Ingredient


class CoffeeMachine():

    _ingredients = {
        "water": (Ingredient("water", "ml"), 300),
        "milk": (Ingredient("milk", "ml"), 500),
        "coffee": (Ingredient("coffee", "g"), 1000),
        "honey": (Ingredient("honey", "oz"), 50),
    }

    _drinks = {
        "espresso": {
            "price": 2.50,
            "ingredients": {
                "water": 10,
                "milk": 40,
                "coffee": 200
            }
        },
        "latte": {
            "price": 1.00,
            "ingredients": {
                "water": 10,
                "milk": 100,
                "coffee": 50
            },
        },
        "cappuccino": {
            "price": 1.50,
            "ingredients": {
                "water": 10,
                "milk": 50,
                "coffee": 80
            }
        },
        "tea": {
            "price": 0.50,
            "ingredients": {
                "honey": 5,
            }
        },
    }

    is_on = False
    _cash = 0

    def __init__(self):
        self.turn_on()

    def _get_remaining_of_ingredient(self, ingredient):
        return self._ingredients[ingredient][1]
    
    def get_drink_list(self):
        return self._drinks
    
    def can_make_drink(self, drink_to_check):
        """Check to see if the machine has enough ingredients for the specified drink"""
        #need to throw an error here if drink comes in thats not on the list
        for drink in self._drinks:
            if drink_to_check != drink:
                continue
            else:
                for ingredient in self._drinks[drink]['ingredients']:
                    if self._drinks[drink]['ingredients'][ingredient] > self._ingredients[ingredient][1]:
                        return False
                else:
                    return True


    def get_ingredient_report(self):
        report = {}
        for ingredient in self._ingredients:  # iterates through the keys
            report[ingredient] = (
                self._ingredients[ingredient][1], self._ingredients[ingredient][0].get_uom())

        report["cash"] = self._cash
        return report
    
    def make_drink(self, drink_to_make):
        for ingredient in self._drinks[drink_to_make]['ingredients']:
            uom_of_ingredient = self._ingredients[ingredient][0].get_uom()
            remaining_qty = self._ingredients[ingredient][1]
            new_qty = (remaining_qty - self._drinks[drink_to_make]['ingredients'][ingredient])
            self._ingredients[ingredient] = (Ingredient(ingredient, uom_of_ingredient), new_qty)

    def turn_on(self):
        print("The coffee machine is turning on...")
        self.is_on = True

    def turn_off(self):
        print("The coffee machine is turning off...")
        self.is_on = False

    def machine_is_on(self):
        return self.is_on
