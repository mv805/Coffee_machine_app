class Ingredient():
    """
    An ingredient with UOM
    """

    def __init__(self, ingredient_name, unit_of_measure):
        self._ingredient_name = ingredient_name
        self._unit_of_measure = unit_of_measure
    
    def get_name(self):
        return self._ingredient_name
    
    def get_uom(self):
        return self._unit_of_measure