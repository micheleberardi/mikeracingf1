# MikeRacingF1 Package

The `MikeRacingF1` package is a Python package that provides a simple and easy-to-use interface to the F1Stats API. The F1Stats API provides data about Formula 1 races, circuits, constructors, drivers, and more.

## Installation

```python
pip install mikeracingf1

```
# Usage
To use the MikeRacingF1 package, you first need to import the MikeRacingF1 class:

```python
from MikeRacingF1 import MikeRacingF1
```

You can then create a new instance of the MikeRacingF1 class, which provides methods for accessing the F1Stats API:

```python
f1stats = MikeRacingF1()
```
The MikeRacingF1 class provides the following methods:

`get_circuits(year):` Returns information about F1 circuits for the given year.

`get_constructor_results(year):` Returns results for F1 constructors for the given year.

`get_constructor_list():` Returns a list of F1 constructors.

`get_constructorstandings():` Returns standings for F1 constructors.

`get_driversinfo(year):` Returns information about F1 drivers for the given year.

`get_driverstandings(year):` Returns standings for F1 drivers for the given year.

`get_races(year):` Returns information about F1 races for the given year.

`get_results(year, round):` Returns results for an F1 race for the given year and round.

Each method sends a GET request to the corresponding endpoint of the F1Stats API, and returns the JSON response as a Python object.

Here's an example of how to use the MikeRacingF1 class to retrieve information about F1 races and circuits:

```python
from MikeRacingF1 import MikeRacingF1

f1stats = MikeRacingF1()

# Retrieve information about F1 circuits for the year 2023
circuits = f1stats.get_circuits(2023)
print("Circuits:")
print(circuits)
print()

# Retrieve information about F1 races for the year 2023
races = f1stats.get_races(2023)
print("Races:")
print(races)
print()
    
 ```
This code creates a new instance of the MikeRacingF1 class, and calls its get_circuits and get_races methods with the year 2023. It then prints the JSON responses from the F1Stats API.

# TEST CODE UNITEST
```python
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
```
This code defines a TestMikeRacingF1 class that subclasses unittest.TestCase. The class includes a setUp method that creates a new instance of the MikeRacingF1 class for each test.

The TestMikeRacingF1 class includes a test method for each of the methods in the MikeRacingF1 class. Each test method sends a request to the corresponding API endpoint and checks that the response is a non-empty list.

The main block at the end of the file runs the unit tests when the file is executed.

You can run the tests by executing the file or using a test runner such as unittest or pytest. For example, to run the tests with unittest, you can execute the following command in your terminal:

```python
python -m unittest test_MikeRacingF1.py
```



License
This package is licensed under the MIT License. See the LICENSE file for details.





