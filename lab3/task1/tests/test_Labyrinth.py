import unittest
from lab3.task1.src.Labyrinth import *


class TestLabyrinth(unittest.TestCase):

    def setUp(self):
        self.labyrinth = Labyrinth()

    def test_graph_builder_minimal_input(self):
        # given
        self.labyrinth.input_file = ["2 1", "1 2", "1 2"]
        expected_graph = {1: {2}, 2: {1}, 3: set(), 4: set()}

        # when
        graph = self.labyrinth.graph_builder()

        # then
        self.assertEqual(graph, expected_graph)

    def test_path_finder_exists(self):
        # given
        self.labyrinth.graph = {1: {2}, 2: {1}}
        self.labyrinth.start = 1
        self.labyrinth.end = 2

        # when
        result = self.labyrinth.path_finder()

        # then
        self.assertEqual(result, 1)  # Путь существует

    def test_path_finder_does_not_exist(self):
        # given
        self.labyrinth.graph = {1: {2}, 2: {1}}
        self.labyrinth.start = 1
        self.labyrinth.end = 3  # Необъединенная вершина

        # when
        result = self.labyrinth.path_finder()

        # then
        self.assertEqual(result, 0)  # Путь не существует

    def test_graph_builder_maximal_input(self):
        # given
        self.labyrinth.n = 1000
        self.labyrinth.m = 1000
        self.labyrinth.input_file = ["1000 1000"] + [f"{i} {i + 1}" for i in range(1, 1000)] + ["1 1000"]

        # when
        graph = self.labyrinth.graph_builder()

        # then
        self.assertEqual(len(graph), 1000)
        self.assertEqual(len(graph[1]), 1)
        self.assertEqual(len(graph[1000]), 1)

    def test_resulting_function_path_exists(self):
        # given
        self.labyrinth.input_file = ["4 4", "1 2", "2 3", "2 4", "4 1", "1 4"]

        # when
        result = self.labyrinth.resulting_function()

        # then
        self.assertEqual(result, 1)  # Путь между 1 и 4 существует

    def test_resulting_function_path_does_not_exist(self):
        # given
        self.labyrinth.input_file = ["4 2", "1 2", "2 3", "1 4"]

        # when
        result = self.labyrinth.resulting_function()

        # then
        self.assertEqual(result, 0)  # Путь между 1 и 4 не существует


if __name__ == '__main__':
    unittest.main()
