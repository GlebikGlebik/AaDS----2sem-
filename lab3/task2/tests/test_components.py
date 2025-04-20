import unittest
from lab3.task2.src.components import *


class TestLabyrinth(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()

    def test_graph_builder_minimum_input(self):
        # given
        self.lab.input_file = ["1 0"]  # 1 вершина, 0 ребер


        # when
        graph = self.lab.resulting_function()

        # then
        self.assertEqual(graph, 1)  # Ожидаем, что граф будет состоять только из одной вершины

    def test_graph_builder_multiple_edges(self):
        # given
        self.lab.input_file = ["3 2", "1 2", "1 3"]  # 3 вершины, 2 ребра
        self.lab.graph = {}

        # when
        graph = self.lab.graph_builder()

        # then
        self.assertEqual(graph, {1: {2}, 2: {1}})  # Проверяем связь между вершинами

    def test_components_counter_single_component(self):
        # given
        self.lab.graph = {1: {2}, 2: {1, 3}, 3: {2}}  # Полный граф
        # when
        count = self.lab.components_counter()

        # then
        self.assertEqual(count, 1)  # Один компонент связности

    def test_components_counter_multiple_components(self):
        # given
        self.lab.graph = {1: {2}, 2: {1}, 3: {4}, 4: {3}}  # Два отдельных компонента
        # when
        count = self.lab.components_counter()

        # then
        self.assertEqual(count, 2)  # Два компонента связности

    def test_resulting_function_empty_graph(self):
        # given
        self.lab.input_file = ["1 0", ""]  # 1 вершина, 0 ребер

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 1)  # Должен вернуть 1, так как есть одна изолированная вершина

    def test_resulting_function_maximum_input(self):
        # given
        n = 1000  # максимальное количество вершин
        edges = ["{} {}".format(i, i + 1) for i in range(1, n)]  # создаем цепочку из n вершин
        input_data = [f"{n} {n - 1}"] + edges

        self.lab.input_file = input_data
        self.lab.graph = {}

        # when
        result = self.lab.resulting_function()

        # then
        self.assertEqual(result, 1)  # Вся цепочка - один компонент связности


if __name__ == '__main__':
    unittest.main()
