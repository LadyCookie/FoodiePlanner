import unittest

from src.cliqual.cliqual_api import CliqualAPI

class TestAPILoading(unittest.TestCase):
    def test_initialize_api(self):
        API = CliqualAPI()
        self.assertTrue(True)
        
class TestSourcesAPI(unittest.TestCase):
    API = CliqualAPI()

    def test_get_sources_with_int(self):
        src = self.API.get_source(4)
        self.assertEqual(src," Valeur ajustée/calculée/imputée Ciqual ")

    def test_get_sources_with_str(self):
        src = self.API.get_source("13")
        self.assertEqual(src, " Calculs Ciqual (2007). ")

    def test_get_invalide_sources(self):
        src = self.API.get_source(" 4 ")
        self.assertIsNone(src)



if __name__ == "__main__":
    unittest.main()