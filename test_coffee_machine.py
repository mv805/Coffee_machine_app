from coffee_machine import CoffeeMachine
from ingredient import Ingredient
import unittest


class TestCoffeeMachine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.machine = CoffeeMachine()

    def test_if_drink_can_be_made(self):
        self.machine._ingredients = {
            "water": (Ingredient("water", "ml"), 300),
            "milk": (Ingredient("milk", "ml"), 50),
            "coffee": (Ingredient("coffee", "g"), 1000),
            "honey": (Ingredient("honey", "oz"), 50),
        }

        self.assertEqual(self.machine.can_make_drink('espresso'), True)
        self.assertEqual(self.machine.can_make_drink('latte'), False)
        self.assertEqual(self.machine.can_make_drink('tea'), True)
    
    def test_that_drink_was_made(self):
        self.machine.make_drink('espresso')
        
        self.assertEqual(290, self.machine._ingredients['water'][1])
        self.assertEqual(10, self.machine._ingredients['milk'][1])
        self.assertEqual(800, self.machine._ingredients['coffee'][1])
    
    def test_raises_error_if_drink_not_avaliable(self):
        self.assertRaises(Exception, self.machine.make_drink, "Test drink")


    @classmethod
    def tearDownClass(cls):
        del cls.machine
        
class TestCoffeeMachineErrors(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.machine = CoffeeMachine()

    def test_raises_error_if_drink_not_avaliable(self):
        self.assertRaises(Exception, self.machine.make_drink, "Test drink")


    @classmethod
    def tearDownClass(cls):
        del cls.machine


if __name__ == '__main__':
    unittest.main()
