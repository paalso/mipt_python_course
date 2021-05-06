# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    def test_even_for_positive_evens(self):
        self.assertTrue(lib.even(2))
        self.assertTrue(lib.even(4))
        self.assertTrue(lib.even(6))
        self.assertTrue(lib.even(3561616))

    def test_even_for_negative_evens(self):
        self.assertTrue(lib.even(-2))
        self.assertTrue(lib.even(-4))

    def test_even_for_positive_odds(self):
        self.assertFalse(lib.even(1))
        self.assertFalse(lib.even(654169))

    def test_even_for_negative_odds(self):
        self.assertFalse(lib.even(-1))
        self.assertFalse(lib.even(-11))

    def test_even_for_zero(self):
        self.assertTrue(lib.even(0))

    def test_even_result_instance(self):
        self.assertIsInstance(lib.even(0), bool)
        self.assertIsInstance(lib.even(2), bool)
        self.assertIsInstance(lib.even(3), bool)
        self.assertIsInstance(lib.even(7), bool)
        self.assertIsInstance(lib.even(-1), bool)
        self.assertIsInstance(lib.even(-2), bool)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
