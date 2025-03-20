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
        result = self.ap.almost_palindromes_counter()

        # then
        self.assertEqual(result, 13)  # Ожидаемое количество почти палиндромов

    def test_expl_1(self):
        # given
        self.ap.n = 5
        self.ap.k = 1
        self.ap.s = 'abcde'

        # when
        result = self.ap.almost_palindromes_counter()

        # then
        self.assertEqual(result, 12)  # Ожидаемое количество почти палиндромов

    def test_expl_2(self):
        # given
        self.ap.n = 3
        self.ap.k = 3
        self.ap.s = 'aaa'

        # when
        result = self.ap.almost_palindromes_counter()

        # then
        self.assertEqual(result, 6)  # Ожидаемое количество почти палиндромов

    def test_guiding_function(self):
        # given
        self.ap.n = 4
        self.ap.k = 1
        self.ap.s = 'aaaa'

        # when
        result = self.ap.almost_palindromes_counter()

        # then
        self.assertEqual(result, 10)  # Ожидаемое количество почти палиндромов

    def test_single_character(self):
        # given
        self.ap.n = 1
        self.ap.k = 0
        self.ap.s = 'a'

        # when
        self.ap.almost_palindromes_counter()

        # then
        self.assertEqual(self.ap.almost_palindromes_counter(), 1)  # Один символ - это палиндром

    def test_maximum_values(self):
        # given
        self.ap.n = 3000  # Максимальное значение N
        self.ap.k = 1  # Максимальное значение K
        self.ap.s = 'a' * 3000 # Строка из 5000 символов 'a'

        # when
        self.ap.almost_palindromes_counter()  # Генерируем подстроки
        expected_result = 4501500

        # then
        result = self.ap.almost_palindromes_counter()  # количество палиндромов в строке из одинаковых символов

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()