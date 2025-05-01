import unittest
from lab4.task1.src.naive_search import *  # Импортируйте ваш класс из правильного модуля


class TestNaiveSearch(unittest.TestCase):

    def setUp(self):
        self.ns = NaiveSearch()

    def test_substring_search_exact_match(self):
        # given
        self.ns.substr = "abc"  # Подстрока для поиска
        self.ns.string = "abcde"  # Строка, в которой ищем

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 1)  # Ожидаем 1 совпадение
        self.assertEqual(indexes, [1])  # Ожидаем, что совпадение на позиции 1

    def test_substring_search_no_match(self):
        # given
        self.ns.substr = "xyz"  # Подстрока для поиска
        self.ns.string = "abcde"  # Строка, в которой ищем

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 0)  # Ожидаем 0 совпадений
        self.assertEqual(indexes, [])  # Ожидаем пустой список индексов

    def test_substring_search_multiple_matches(self):
        # given
        self.ns.substr = "aa"  # Подстрока для поиска
        self.ns.string = "aaaaa"  # Строка, в которой ищем

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 4)  # Ожидаем 4 совпадения
        self.assertEqual(indexes, [1, 2, 3, 4])  # Ожидаем совпадения на позициях 1, 2, 3, 4

    def test_substring_search_empty_string(self):
        # given
        self.ns.substr = "abc"  # Подстрока для поиска
        self.ns.string = ""  # Пустая строка

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 0)  # Ожидаем 0 совпадений
        self.assertEqual(indexes, [])  # Ожидаем пустой список индексов

    def test_substring_search_empty_substring(self):
        # given
        self.ns.substr = "a"  # Пустая подстрока
        self.ns.string = "abcde"  # Строка, в которой ищем

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 1)  # Ожидаем 0 совпадений
        self.assertEqual(indexes, [1])  # Ожидаем пустой список индексов

    def test_substring_search_minimum_input(self):
        # given
        self.ns.substr = "a"  # Минимальная подстрока
        self.ns.string = "a"  # Минимальная строка

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count, 1)  # Ожидаем 1 совпадение
        self.assertEqual(indexes, [1])  # Ожидаем совпадение на позиции 1

    def test_substring_search_maximum_input(self):
        # given
        self.ns.substr = "a" * 1000  # Максимальная подстрока
        self.ns.string = "a" * 10000  # Максимальная строка

        # when
        count, indexes = self.ns.substring_search()

        # then
        self.assertEqual(count,  9001)  # Ожидаем 9901 совпадение

if __name__ == '__main__':
    unittest.main()
