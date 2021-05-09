import unittest


def find_next(L, i):
    for j in range(i + 1, len(L)):
        if L[j] == - L[i]:
            return j - i


class FindNextTestCase(unittest.TestCase):

    def test_find_next(self):
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 0), 5)
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 1), 2)
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 2), 2)
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 3), None)
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 4), None)
        self.assertEqual(find_next([-40, 41, -42, -41, 42, 40], 5), None)


unittest.main(verbosity=2)
