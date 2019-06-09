import unittest
from unittest import mock
from fibonacci import my_functions


class Test102(unittest.TestCase):
    def test_sequence(self):
        first_29 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                    610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                    46368, 75025, 121393, 196418, 317811]
        self.assertEqual(first_29[28], my_functions.fibonacci(28))

    def test_ask(self):
        with mock.patch('builtins.input', return_value='28'):
            self.assertEqual(28, my_functions.ask_how_many())

    def test_ask_is_not_int(self):
        with mock.patch('builtins.input', return_value='2.8'):
            with self.assertRaises(ValueError, msg='Value is not an integer'):
                my_functions.ask_how_many()

    def test_ask_is_neg(self):
        with mock.patch('builtins.input', return_value='-12'):
            with self.assertRaises(ValueError, msg='Value is not a positive integer'):
                my_functions.ask_how_many()

    def test_ask_txt_number(self):
        with mock.patch('builtins.input', return_value='ten'):
            with self.assertRaises(ValueError, msg='Value is not a positive integer'):
                my_functions.ask_how_many()


if __name__ == '__main__':
    unittest.main(verbosity=2)
