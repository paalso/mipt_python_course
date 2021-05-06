# Подключаем библиотеку для тестирования
import unittest

import math, random

# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    def test_sin_positive_arg(self):
        self.assertAlmostEqual(lib.sin(0), math.sin(0))
        self.assertAlmostEqual(lib.sin(math.pi / 6), math.sin(math.pi / 6))
        self.assertAlmostEqual(lib.sin(math.pi / 4), math.sin(math.pi / 4))
        self.assertAlmostEqual(lib.sin(math.pi / 3), math.sin(math.pi / 3))
        self.assertAlmostEqual(lib.sin(math.pi / 2), math.sin(math.pi / 2))
        self.assertAlmostEqual(lib.sin(math.pi), math.sin(math.pi))
        self.assertAlmostEqual(lib.sin(3 * math.pi / 2), math.sin(3 * math.pi / 2))
        self.assertAlmostEqual(lib.sin(2 * math.pi), math.sin(2 * math.pi))
        self.assertAlmostEqual(lib.sin(3 * math.pi), math.sin(3 * math.pi))

    def test_sin_negative_arg(self):
        self.assertAlmostEqual(lib.sin(- math.pi / 4), math.sin(- math.pi / 4))
        self.assertAlmostEqual(lib.sin(- math.pi / 2), math.sin(- math.pi / 2))
        self.assertAlmostEqual(lib.sin(- math.pi), math.sin(- math.pi))
        self.assertAlmostEqual(lib.sin(- 3 * math.pi / 2), math.sin(- 3 * math.pi / 2))

    def test_sin_int_positive_degrees(self):
        for n in range(360):
            x = math.radians(n / 360)
            self.assertAlmostEqual(lib.sin(x), math.sin(x))

    def test_sin_int_negative_degrees(self):
        for n in range(360):
            x = - math.radians(n / 360)
            self.assertAlmostEqual(lib.sin(x), math.sin(x))

    def test_sin_random_arg(self):
        x = random.random() * 1000000
        for _ in range(100):
            self.assertAlmostEqual(lib.sin(x), math.sin(x))


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
