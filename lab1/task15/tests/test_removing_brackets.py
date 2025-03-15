import unittest
from lab1.task15.src.removing_brackets import *

class TestRemovingBrackets(unittest.TestCase):

    def setUp(self):
        self.rem = Removing()

    def test_add_and_exists(self):
        # given
        self.s = '(][{()(()))))}]'
        expected_result = '[{()(())}]'

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_minimum_input(self):
        # given
        self.s = '('
        expected_result = ''  # ничего не остается

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_maximum_input(self):
        # given
        self.s = '(){}[]' * 10  # 60 символов (максимум 100)
        expected_result = '(){}[]' * 10  # все скобки должны остаться

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_unmatched_brackets(self):
        # given
        self.s = '([)]'
        expected_result = '[]'

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_nested_brackets(self):
        # given
        self.s = '((()))'
        expected_result = '((()))'  # Все скобки должны остаться

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_complex_case(self):
        # given
        self.s = '{([])}'
        expected_result = '{([])}'  # Все скобки должны остаться

        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

    def test_100_elements(self):
        # given
        self.s = '([){]]))[{[][)]{(}}){([{][[[[)(()}}]](][}(}}[}{)}(}{)}[()[[]]{][[{){{})[{{))[(({[]][))}})([)([][{{(['
        expected_result = '[][]()(){}{}()[[]]{}[][]'
        # when
        self.rem.s = self.s
        result = self.rem.resulting_function()

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
