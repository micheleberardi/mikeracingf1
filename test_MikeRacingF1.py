import unittest
from mikeracingf1 import MikeRacingF1
#### python -m unittest test_MikeRacingF1.py

class TestMikeRacingF1(unittest.TestCase):

    def setUp(self):
        self.f1stats = MikeRacingF1()

    def test_get_circuits(self):
        year = 2022
        circuits = self.f1stats.get_circuits(year)
        self.assertIsInstance(circuits, list)
        self.assertGreater(len(circuits), 0)

    def test_get_constructor_results(self):
        year = 2022
        constructor_results = self.f1stats.get_constructor_results(year)
        self.assertIsInstance(constructor_results, list)
        self.assertGreater(len(constructor_results), 0)

    def test_get_constructor_list(self):
        constructor_list = self.f1stats.get_constructor_list()
        self.assertIsInstance(constructor_list, list)
        self.assertGreater(len(constructor_list), 0)

    def test_get_constructorstandings(self):
        constructor_standings = self.f1stats.get_constructorstandings()
        self.assertIsInstance(constructor_standings, list)
        self.assertGreater(len(constructor_standings), 0)

    def test_get_driversinfo(self):
        year = 2022
        drivers_info = self.f1stats.get_driversinfo(year)
        self.assertIsInstance(drivers_info, list)
        self.assertGreater(len(drivers_info), 0)

    def test_get_driverstandings(self):
        year = 2022
        driver_standings = self.f1stats.get_driverstandings(year)
        self.assertIsInstance(driver_standings, list)
        self.assertGreater(len(driver_standings), 0)

    def test_get_races(self):
        year = 2022
        races = self.f1stats.get_races(year)
        self.assertIsInstance(races, list)
        self.assertGreater(len(races), 0)

    def test_get_results(self):
        year = 2022
        race_round = 1
        results = self.f1stats.get_results(year, race_round)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

if __name__ == '__main__':
    unittest.main()
