import unittest
from tyres import my_functions


class Test302(unittest.TestCase):

    def test_tyre_details(self):
        tyre_specs = ['255/45W17', '155/70N12', '225/40Y18', '215/65R16',
                      '125/85R16', '205/55ZR16']
        tyre_details = [
            {'width': 255, 'profile': 45, 'rating': 'W', 'rim': 17},
            {'width': 155, 'profile': 70, 'rating': 'N', 'rim': 12},
            {'profile': 40, 'rating': 'Y', 'rim': 18, 'width': 225},
            {'profile': 65, 'rating': 'R', 'rim': 16, 'width': 215},
            {'profile': 85, 'rating': 'R', 'rim': 16, 'width': 125},
            {'width': 205, 'profile': 55, 'rating': 'ZR', 'rim': 16},
        ]
        for i, tyre_spec in enumerate(tyre_specs):
            with self.subTest(val=tyre_spec):
                self.assertDictEqual(tyre_details[i],
                                     my_functions.tyre_details(tyre_spec))

    def test_speed_index(self):
        spd_i = [['ZR', '> 240 km/h'],
                 ['S', '180 km/h'],
                 ['M', '130 km/h']]
        for i, spd in spd_i:
            with self.subTest(val=i):
                self.assertEqual(spd, my_functions.speed_index(i))


if __name__ == '__main__':
    unittest.main(verbosity=2)
