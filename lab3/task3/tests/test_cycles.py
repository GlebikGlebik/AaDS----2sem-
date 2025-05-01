import unittest
from lab3.task3.src.cycles import *


class TestLabyrinth(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()

    def test_graph_builder_minimum_input(self):
        # given
        self.lab.input_file = ["1 0"]  # 1 вершина, 0 ребер

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 0)  # Ожидаем, что граф не содержит циклов

    def test_graph_builder_single_cycle(self):
        # given
        self.lab.input_file = ["2 2", "1 2", "2 1"]  # 2 вершины, 2 ребра

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 1)  # Ожидаем, что граф содержит цикл

    def test_graph_builder_multiple_edges(self):
        # given
        self.lab.input_file = ["3 3", "1 2", "2 3", "3 1"]  # Цикл между тремя вершинами

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 1)  # Ожидаем, что граф содержит цикл

    def test_graph_builder_no_cycle(self):
        # given
        self.lab.graph = {1: [2], 2: [3], 3: [4]} # Линейная структура без цикла

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 0)  # Ожидаем, что граф не содержит циклов

    def test_resulting_function_maximum_input_no_cycle(self):
        # given
        n = 1000  # максимальное количество вершин
        self.lab.graph = {i: [i + 1] for i in range(1, n)}  # создаем линейную цепочку
        self.lab.graph[n] = []  # Последняя вершина не имеет рёбер

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 0)  # Вся цепочка не содержит циклов

if __name__ == '__main__':
    unittest.main()
