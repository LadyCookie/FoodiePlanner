import unittest

from cliqual.cliqual_api import CliqualAPI

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

    def test_get_specific_compo_with_int(self):
        component = self.API.get_specific_compo(9810,328)
        self.assertEqual(component.element, " Energie, Règlement UE N° 1169/2011 (kcal/100 g) ")
        self.assertEqual(component.content, 336.0)
        self.assertEqual(component.trust_code, " C ")
        self.assertEqual(component.source, ' Valeur ajustée/calculée/imputée Ciqual ')
        self.assertEqual(component.min, None)
        self.assertEqual(component.max, None)

class TestGroupAPI(unittest.TestCase):
    API = CliqualAPI(load_everything = False, load_alim_grp = True)

    def test_get_grp_with_group(self):
        grp = self.API.get_group(4,410,41003)
        self.assertEqual(grp.group, ' viandes, oeufs, poissons et assimilés ')
        self.assertEqual(grp.subgroup, ' oeufs ')
        self.assertEqual(grp.subsubgroup, ' omelettes et autres ovoproduits ')

class TestAlimAPI(unittest.TestCase):
    API = CliqualAPI()

    def test_get_aliment_with_int(self):
        alim = self.API.get_aliment(1000)
        self.assertEqual(alim.name, ' Pastis ')

if __name__ == "__main__":
    unittest.main()