# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    def test_factorial_non_negative_arg(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(2), 2)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(4), 24)
        self.assertEqual(lib.factorial(5), 120)
        self.assertEqual(lib.factorial(6), 720)

    def test_factorial_negative_minus_one(self):
        self.assertEqual(lib.factorial(-1), 1)

    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-10), 1)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
