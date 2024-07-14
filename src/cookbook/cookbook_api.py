import xml.etree.ElementTree as etree
import model

class Recipe:
    #------------#
    # ATTRIBUTES #
    #------------#
    _NAME = ""
    _PORTION = 0
    _COOKING_TIME = 0
    _COMPOSITION = []
    _RECIPE = []

    #--------------#
    # INITIALISERS #
    #--------------#

    def __init__(self, file_path = ""):
        print("...loading xml at " + file_path)
        recipe_tree = etree.parse(file_path)

        name = recipe_tree.find(".//INFO/name")
        self._NAME = "" if name is None else name.text

        portion = recipe_tree.find(".//INFO/portion")
        self._PORTION = "0" if portion is None else portion.text

        cooking_time = recipe_tree.find(".//INFO/cooking_time")
        self._COOKING_TIME = "0" if cooking_time is None else cooking_time.text

        composition = recipe_tree.findall(".//COMPO/INGREDIENT")
        #self._COMPOSITION = [] if composition is None else composition.text
        recipe = recipe_tree.findall(".//RECIPE/STEP")
        #self._RECIPE = [] if recipe is None else recipe.text 