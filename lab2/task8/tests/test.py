import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from lab2.task8.src.heightOfTheTree import TreeHeightSolver

class TestTreeHeightSolver(unittest.TestCase):
    def setUp(self):
        self.task = 8

    def run_solver(self, input_lines):
        solver = TreeHeightSolver(self.task, input_data=input_lines)
        return solver.solve()

    def test_example_case(self):
        input_data = [
            "6",
            "-2 0 2",
            "8 4 3",
            "9 0 0",
            "3 6 5",
            "6 0 0",
            "0 0 0"
        ]
        expected = 4
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    def test_empty_tree(self):
        input_data = ["0"]
        expected = 0
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    def test_single_node_tree(self):
        input_data = [
            "1",
            "10 0 0"
        ]
        expected = 1
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    def test_left_skewed_tree(self):
        input_data = [
            "3",
            "10 2 0",
            "5 3 0",
            "1 0 0"
        ]
        expected = 3
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

    def test_right_skewed_tree(self):
        input_data = [
            "3",
            "1 0 2",
            "5 0 3",
            "10 0 0"
        ]
        expected = 3
        result = self.run_solver(input_data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()