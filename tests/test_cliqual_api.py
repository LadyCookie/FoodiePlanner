import unittest

from src.cliqual.cliqual_api import CliqualAPI

class TestAPILoading(unittest.TestCase):
    def test_initialize_api(self):
        API = CliqualAPI()
        self.assertTrue(True)
        

if __name__ == "__main__":
    unittest.main()