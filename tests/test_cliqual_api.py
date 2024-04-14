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

    def test_get_invalid_sources(self):
        src = self.API.get_source(" 4 ")
        self.assertIsNone(src)

class TestConstAPI(unittest.TestCase):
    API = CliqualAPI(load_everything = False, load_const = True)

    def test_get_const_with_int(self):
        src = self.API.get_const(400)
        self.assertEqual(src," Eau (g/100 g) ")

    def test_get_const_with_str(self):
        src = self.API.get_const("60000")
        self.assertEqual(src," Alcool (g/100 g) ")

    def test_get_invalid_const(self):
        src = self.API.get_const(" 56600 ")
        self.assertIsNone(src)

if __name__ == "__main__":
    unittest.main()