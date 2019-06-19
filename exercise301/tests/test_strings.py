import os
import unittest
from strings import my_functions


class Test301(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_file1 = os.path.join(self.test_dir, 'data_1.txt')

    def test_find_years(self):
        result = my_functions.find_year(self.test_file1)
        self.assertListEqual(['1992'], result)

    def test_find_email(self):
        expected = ['Proin@tempor.augue.arcu', 'tristique@sit.amet']
        result = my_functions.find_email(self.test_file1)
        self.assertListEqual(expected, result)

    def test_find_initial_caps(self):
        expected = ['Lorem',
                    'Ipsum',
                    'Neque',
                    'There',
                    'Aliquam',
                    'Nulla',
                    'Donec',
                    'Vestibulum',
                    'Sed',
                    'Aenean',
                    'Aenean',
                    'Mauris',
                    'Sed',
                    'Proin',
                    'Proin',
                    'Etiam',
                    'Aliquam',
                    'Pellentesque',
                    'Fusce',
                    'Nunc',
                    'Ut',
                    'Donec',
                    'Nam',
                    'In',
                    'In',
                    'Sed',
                    'Sed',
                    'Vestibulum',
                    'Proin',
                    'Ut',
                    'Etiam',
                    'Vivamus',
                    'Morbi',
                    'Ut',
                    'Fusce',
                    'Vivamus',
                    'Aenean']

        result = my_functions.find_initial_caps(self.test_file1)
        self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
