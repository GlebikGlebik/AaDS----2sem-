import unittest
from lab4.task2.src.map import *  # Импортируйте ваш класс из правильного модуля


class TestMap(unittest.TestCase):

    def setUp(self):
        self.map_instance = Map()

    def test_map_decoder_minimum_input(self):
        # given
        self.map_instance.string = "a"  # Минимальная строка
        self.map_instance.new_string = self.map_instance.string.replace(' ', '')

        # when
        result = self.map_instance.resulting_function()

        # then
        self.assertEqual(result, 0)  # Ожидаем 0 палиндромов

    def test_map_decoder_single_palindrome(self):
        # given
        self.map_instance.string = "abc"  # Строка без палиндромов
        self.map_instance.new_string = self.map_instance.string.replace(' ', '')

        # when
        result = self.map_instance.resulting_function()

        # then
        self.assertEqual(result, 0)  # Ожидаем 0 палиндромов

    def test_map_decoder_multiple_palindromes(self):
        # given
        self.map_instance.string = "abababa"  # Палиндромы: "aba", "bab", "aba"
        self.map_instance.new_string = self.map_instance.string.replace(' ', '')

        # when
        result = self.map_instance.resulting_function()

        # then
        self.assertEqual(result, 19)  # Ожидаем 5 палиндромов: "aba", "bab", "aba", "ababa", "abababa"

    def test_map_decoder_empty_string(self):
        # given
        self.map_instance.string = ""  # Пустая строка
        self.map_instance.new_string = self.map_instance.string.replace(' ', '')

        # when
        result = self.map_instance.resulting_function()

        # then
        self.assertEqual(result, 0)  # Ожидаем 0 палиндромов

    def test_map_decoder_maximum_input(self):
        # given
        self.map_instance.string = "a" * 300  # Максимальная строка с 300000 символов "a"
        self.map_instance.new_string = self.map_instance.string.replace(' ', '')

        # when
        result = self.map_instance.resulting_function()

        # then
        # Каждый выбор из трех "a" будет палиндромом, для n a = n * (n - 1) * (n - 2) / 6
        expected_result = 300 * (300 - 1) * (300 - 2) // 6  # Ожидаемое количество палиндромов

        self.assertEqual(result, expected_result)  # Проверяем, равно ли количество ожидаемому


if __name__ == '__main__':
    unittest.main()
