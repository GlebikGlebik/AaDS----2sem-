import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from lab1.task10.src.apples import ApplesSolver

class TestApplesSolver(unittest.TestCase):
    def setUp(self):
        self.task = 10

    def run_solver(self, input_lines):
        solver = ApplesSolver(self.task, input_data=input_lines)
        return solver.solve()

    # Тест из условия задачи (ожидается порядок 1 3 2)
    def test_example_case(self):
        input_data = [
            "3 5",
            "2 3",
            "10 5",
            "5 10"
        ]
        expected = [1, 3, 2]
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    # Тест с невозможным случаем
    def test_impossible_case(self):
        input_data = [
            "3 5",
            "2 3",
            "10 5",
            "5 6"  # После сортировки приведет к отрицательному росту
        ]
        result = self.run_solver(input_data)
        self.assertEqual(result, -1)

    # Все яблоки из группы A (увеличивающие рост)
    def test_all_group_a(self):
        input_data = [
            "3 10",
            "2 5",  # a=2, b=5 (idx 1)
            "3 7",  # a=3, b=7 (idx 2)
            "1 4"   # a=1, b=4 (idx 3)
        ]
        # Ожидаемый порядок: сортировка по a_i: 3,1,2 -> индексы [3,1,2]
        expected = [3, 1, 2]
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    # Все яблоки из группы B (уменьшающие рост)
    def test_all_group_b(self):
        input_data = [
            "2 10",
            "5 3",  # a=5, b=3 (idx 1)
            "4 2"   # a=4, b=2 (idx 2)
        ]
        # Ожидаемый порядок: сортировка по убыванию b_i: 1,2 -> индексы [1,2]
        expected = [1, 2]
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    # Пограничный случай: минимально допустимый рост
    def test_edge_case(self):
        input_data = [
            "1 6",
            "5 10"  # a=5 → 6-5=1 >0 → допустимо
        ]
        expected = [1]
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    # Случай с нулевым ростом после уменьшения
    def test_zero_height(self):
        input_data = [
            "1 5",
            "5 10"  # 5-5=0 → недопустимо
        ]
        result = self.run_solver(input_data)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()