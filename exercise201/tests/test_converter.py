import unittest
from converter import my_functions


class Test201(unittest.TestCase):

    def test_kmh2mph(self):
        speeds = [[30, 18.64, 2],
                  [50, 31.069, 3],
                  [90, 55.9235, 4],
                  [110, 68.4, 1],
                  [130, 81, 0]]
        for kmh, mph, precision in speeds:
            with self.subTest(val=kmh):
                self.assertEqual(mph,
                                 my_functions.kmh_to_mph(kmh, precision))

    def test_mph2kmh(self):
        speeds = [[30, 48.2802, 4],
                  [40, 64.374, 3],
                  [50, 80.47, 2],
                  [60, 96.6, 1],
                  [70, 113, 0]]
        for mph, kmh, precision in speeds:
            with self.subTest(val=mph):
                self.assertEqual(kmh,
                                 my_functions.mph_to_kmh(mph, precision))


if __name__ == '__main__':
    unittest.main(verbosity=2)
