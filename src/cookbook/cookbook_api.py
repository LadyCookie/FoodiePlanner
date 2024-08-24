import xml.etree.ElementTree as etree
import model

class Ingredient:
    #--------------#
    # INITIALISERS #
    #--------------#

    def __init__(self, XML_Ingredient):

        self._NAME = ""
        self._CODE = 0
        self._QUANTITY = 0

        name = XML_Ingredient.find('NOM')
        self._NAME = "" if name is None else name.text
        
        code = XML_Ingredient.find('CODE')
        self._CODE = "" if code is None else code.text 

        quantity = XML_Ingredient.find('QUANTITE')
        self._QUANTITY = "" if quantity is None else quantity.text



class Recipe:
    #--------------#
    # INITIALISERS #
    #--------------#

    def __init__(self, file_path = ""):

        self._NAME = ""
        self._PORTION = 0
        self._COOKING_TIME = 0
        self._COMPOSITION = []
        self._RECIPE = []
        self._SCORE = 0

        print("...loading xml at " + file_path)
        recipe_tree = etree.parse(file_path)

        name = recipe_tree.find(".//INFO/name")
        self._NAME = "" if name is None else name.text

        portion = recipe_tree.find(".//INFO/portion")
        portion_text = "0" if portion is None else portion.text
        self._PORTION = int(portion_text)

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
        total_content = 0
        for ingredient in self._COMPOSITION:
            compo = model.Cliqual_API.get_specific_compo(ingredient._CODE,328)
            total_content += compo.content
        self._SCORE = total_content/self._PORTION
        
