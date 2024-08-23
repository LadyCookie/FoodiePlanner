import xml.etree.ElementTree as etree
import model

class Ingredient:
    #------------#
    # ATTRIBUTES #
    #------------#
    _NAME = ""
    _CODE = 0
    _QUANTITY = 0

    def __init__(self, XML_Ingredient):
        name = XML_Ingredient.find('NOM')
        self._NAME = "" if name is None else name.text
        
        code = XML_Ingredient.find('CODE')
        self._CODE = "" if code is None else code.text 

        quantity = XML_Ingredient.find('QUANTITE')
        self._QUANTITY = "" if quantity is None else quantity.text



class Recipe:
    #------------#
    # ATTRIBUTES #
    #------------#
    _NAME = ""
    _PORTION = 0
    _COOKING_TIME = 0
    _COMPOSITION = []
    _RECIPE = []
    _SCORE = 0

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
        for ingredient in composition:
            new_ingredient = Ingredient(ingredient)
            self._COMPOSITION.append(new_ingredient)

        self.compute_score()

        recipe = recipe_tree.findall(".//RECIPE/STEP")
        #self._RECIPE = [] if recipe is None else recipe.text 

    def compute_score(self):
        self._SCORE = 100