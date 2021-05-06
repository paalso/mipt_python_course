import unittest
from A import find_two_equal


class FindTwoEqual(unittest.TestCase):

    def test_find_two_equal(self):
        self.assertEqual(find_two_equal([8, 3, 5, 4, 5, 1]), 5)
        self.assertEqual(find_two_equal([5, 5, 1, 4, 2, 3]), 5)
        self.assertEqual(find_two_equal([1, 4, 2, 3, 5, 5]), 5)
        self.assertEqual(find_two_equal([5, 5]), 5)
        self.assertEqual(find_two_equal([5, 1, 2, 3, 4, 5]), 5)


unittest.main()
