import unittest
from collections import namedtuple

from bug_hunter import my_functions

TestData = namedtuple('TestData', ['qty', 'result'])


class Test401(unittest.TestCase):
    def test_boxes_required(self):
        data = [TestData(1, 1),
                TestData(11, 2),
                TestData(12, 2),
                TestData(17, 3)]

        for test in data:
            with self.subTest(value=test.qty):
                self.assertEqual(test.result,
                                 my_functions.boxes_required(test.qty))


if __name__ == '__main__':
    unittest.main(verbosity=2)
