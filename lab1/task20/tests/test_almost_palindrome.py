import unittest
from lab1.task20.src.almost_palindrome import *

class TestAlmostPalindrome(unittest.TestCase):

    def setUp(self):
        self.ap = AlmostPalindrome()

    def test_counter_almost_palindrome(self):
        # given
        self.ap.n = 5
        self.ap.k = 1
        self.ap.s = 'abcba'

        # when
        result = self.ap.resulting_function()

        # then
        self.assertEqual(result, 13)  # Ожидаемое количество почти палиндромов

    def test_guiding_function(self):
        # given
        self.ap.n = 4
        self.ap.k = 1
        self.ap.s = 'aaaa'

        # when
        result = self.ap.resulting_function()

        # then
        self.assertEqual(result, 10)  # Ожидаемое количество почти палиндромов

    def test_empty_string(self):
        # given
        self.ap.n = 0
        self.ap.k = 1
        self.ap.s = ''

        # when
        self.ap.resulting_function()

        # then
        self.assertEqual(self.ap.subwords, [])  # Подстрок не должно быть

    def test_single_character(self):
        # given
        self.ap.n = 1
        self.ap.k = 0
        self.ap.s = 'a'

        # when
        self.ap.resulting_function()

        # then
        self.assertEqual(self.ap.counter_almost_palindrome(), 1)  # Один символ - это палиндром

    def test_maximum_values(self):
        # given
        self.ap.n = 5000  # Максимальное значение N
        self.ap.k = 1  # Максимальное значение K
        self.ap.s = 'a' * 5000  # Строка из 5000 символов 'a'

        # when
        self.ap.subword_finder()  # Генерируем подстроки
        expected_result = 5000

        # then
        result = self.ap.counter_almost_palindrome()  # Ожидаемое количество палиндромов в строке из одинаковых символов

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()