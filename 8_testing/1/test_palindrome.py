# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    def test_palindrome_empty_string(self):
        self.assertTrue(lib.palindrome(""))

    def test_palindrome_oneletter_string(self):
        self.assertTrue(lib.palindrome("q"))

    def test_palindrome_evenletters_string(self):
        self.assertTrue(lib.palindrome("qq"))
        self.assertTrue(lib.palindrome("abba"))

    def test_non_palindrome_evenletters_string(self):
        self.assertFalse(lib.palindrome("aq"))
        self.assertFalse(lib.palindrome("abca"))

    def test_palindrome_oddletters_string(self):
        self.assertTrue(lib.palindrome("aba"))
        self.assertTrue(lib.palindrome("abcba"))

    def test_non_palindrome_oddletters_string(self):
        self.assertFalse(lib.palindrome("abcda"))
        self.assertFalse(lib.palindrome("abc"))

    def test_palindrome_string_with_blancs(self):
        self.assertTrue(lib.palindrome("qqq  qqq"))
        self.assertTrue(lib.palindrome("a  a"))
        self.assertTrue(lib.palindrome("ab ba"))

# Запускаем тесты на исполнение
unittest.main(verbosity=2)
