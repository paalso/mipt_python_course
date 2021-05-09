import unittest
from B import find_coins_demand


class FindTwoEqual(unittest.TestCase):

    def test_find_two_equal(self):
        self.assertEqual(find_coins_demand([10, 5, 100]), 19)
        self.assertEqual(find_coins_demand([5, 5, 10]), 0)
        self.assertEqual(find_coins_demand([50, 5, 5, 5]), 9)



unittest.main()
