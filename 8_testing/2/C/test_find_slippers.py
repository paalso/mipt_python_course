import unittest
from C import find_slippers


class FindSlippersTestCase(unittest.TestCase):

    def test_find_slippers(self):
        self.assertEqual(find_slippers([-40, 41, -42, -41, 42, 40]), 2)
        self.assertEqual(find_slippers([-40, 41, -42, 42, -41, 42, 40]), 1)
        self.assertEqual(find_slippers([-40, 40, 41, -42, -41, 42, 40]), 1)
        self.assertEqual(find_slippers([-40, -40, -41, 42, 43, 44]), 0)
        self.assertEqual(find_slippers([40, -40]), 0)
        self.assertEqual(find_slippers([-39, 40, 40, 40, 40, 40, 39]), 6)
        self.assertEqual(find_slippers([-39, 40, 40, 39, -40, 40]), 1)
        self.assertEqual(find_slippers([-39, 39, -40, 39, 39, 40, 40]), 1)


unittest.main()
