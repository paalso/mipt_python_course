##>>> replace('aaa')
##'aaa'
##>>> replace('aaha')
##'aaha'
##>>> replace('aahha')
##'aahha'
##>>> replace('aahhha')
##'aahHha'
##>>> replace('Haahhha')
##'haaHHha'

import unittest
from replace_function import replace


class ReplaceTestCase(unittest.TestCase):
    def test_replace_function_1(self):
        self.assertEqual(replace('aaa'), 'aaa')

    def test_replace_function_2(self):
        self.assertEqual(replace('aaha'), 'aaha')

    def test_replace_function_3(self):
        self.assertEqual(replace('aahhha'), 'aahHha')

    def test_replace_function_4(self):
        self.assertEqual(replace('Haahhha'), 'HaahHha')

    def test_replace_function_5(self):
        self.assertEqual(replace(''), '')


unittest.main(verbosity=2)
