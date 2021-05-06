# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    def test_prime_positive_prime(self):
        self.assertTrue(lib.prime(7))
        self.assertTrue(lib.prime(3))

    def test_prime_zero(self):
        self.assertFalse(lib.prime(0))

    def test_prime_one(self):
        self.assertFalse(lib.prime(1))

    def test_prime_two(self):
        self.assertTrue(lib.prime(2))

    def test_prime_odd_nonprime(self):
        self.assertFalse(lib.prime(9))
        self.assertFalse(lib.prime(21))

    def test_prime_even_nonprime(self):
        self.assertFalse(lib.prime(4))
        self.assertFalse(lib.prime(6))

    def test_prime_negative_quasi_prime(self):
        self.assertFalse(lib.prime(-2))
        self.assertFalse(lib.prime(-3))

    def test_prime_negative(self):
        self.assertFalse(lib.prime(-4))
        self.assertFalse(lib.prime(-8))


# Запускаем тесты на исполнение
unittest.main(verbosity=2                       )
