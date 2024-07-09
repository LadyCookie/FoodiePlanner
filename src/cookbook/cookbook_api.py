import xml.etree.ElementTree as etree

class Recipe:
    #------------#
    # ATTRIBUTES #
    #------------#
    _NAME = ""
    _PREP_TIME = 0
    _COOKING_TIME = 0
    _COMPOSITION = []
    _RECIPE = []

    #--------------#
    # INITIALISERS #
    #--------------#

    def __init__(self, file_path = ""):
        print("...loading xml at " + file_path)
        recipe_tree = etree.parse(file_path)

        self._NAME = recipe_tree.find(".//INFO/name")
        self._PREP_TIME = recipe_tree.find(".//INFO/prep_time")
        self._COOKING_TIME = recipe_tree.find(".//INFO/cooking_time")

        self._COMPOSITION = recipe_tree.findall(".//COMPO/INGREDIENT")
        self._RECIPE = recipe_tree.findall(".//RECIPE/STEP")