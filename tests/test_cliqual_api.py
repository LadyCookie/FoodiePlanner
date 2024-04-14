import unittest

from src.cliqual.cliqual_api import CliqualAPI

class TestAPILoading(unittest.TestCase):
    def test_initialize_api(self):
        API = CliqualAPI()
        self.assertTrue(True)
        
class TestSourcesAPI(unittest.TestCase):
    API = CliqualAPI(load_everything = False, load_sources = True)

    def test_get_sources_with_int(self):
        src = self.API.get_source(4)
        self.assertEqual(src," Valeur ajustée/calculée/imputée Ciqual ")

    def test_get_sources_with_str(self):
        src = self.API.get_source("13")
        self.assertEqual(src, " Calculs Ciqual (2007). ")

    def test_get_sources_with_spaced_str(self):
        src = self.API.get_source(" 4 ")
        self.assertEqual(src," Valeur ajustée/calculée/imputée Ciqual ")

class TestConstAPI(unittest.TestCase):
    API = CliqualAPI(load_everything = False, load_const = True)

    def test_get_const_with_int(self):
        const = self.API.get_const(400)
        self.assertEqual(const," Eau (g/100 g) ")

    def test_get_const_with_str(self):
        const = self.API.get_const("60000")
        self.assertEqual(const," Alcool (g/100 g) ")

    def test_get_const_with_spaced_str(self):
        const = self.API.get_const(" 400 ")
        self.assertEqual(const," Eau (g/100 g) ")

class TestCompoAPI(unittest.TestCase):
    API = CliqualAPI(load_everything = False, load_compo = True, load_sources = True, load_const = True)

    def test_get_compo_with_int(self):
        compo = self.API.get_compo(1000)
        self.assertEqual(len(compo),67)



if __name__ == "__main__":
    unittest.main()