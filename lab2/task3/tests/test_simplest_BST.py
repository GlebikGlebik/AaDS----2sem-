import unittest
from lab2.task3.src.simplest_BST import *


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def test_add_single_node(self):
        # given
        value = 10

        # when
        self.tree.add(value)

        # then
        self.assertEqual(self.tree.root.value, 10)  # Корень должен иметь значение 10

    def test_add_multiple_nodes(self):
        # given
        values = [10, 5, 15, 3, 7, 12, 20]

        # when
        for value in values:
            self.tree.add(value)

        # then
        self.assertEqual(self.tree.root.left.value, 5)
        self.assertEqual(self.tree.root.right.value, 15)
        self.assertEqual(self.tree.root.left.left.value, 3)
        self.assertEqual(self.tree.root.left.right.value, 7)
        self.assertEqual(self.tree.root.right.left.value, 12)
        self.assertEqual(self.tree.root.right.right.value, 20)

    def test_find_min_greater_than_existing_value(self):
        # given
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

        # when
        result = self.tree.find_min_greater_than(10)

        # then
        self.assertEqual(result, 15)  # Ожидаем, что минимальное значение больше 10 - это 15

    def test_find_min_greater_than_non_existing_value(self):
        # given
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

        # when
        result = self.tree.find_min_greater_than(20)

        # then
        self.assertEqual(result, '0')  # Ожидаем, что вернется '0', так как нет значения больше 20

    def test_find_min_greater_than_empty_tree(self):
        # when
        result = self.tree.find_min_greater_than(10)

        # then
        self.assertEqual(result, '0')  # Ожидаем, что вернется '0', так как дерево пустое

    def test_add_duplicate_values(self):
        # given
        self.tree.add(10)
        self.tree.add(5)

        # when
        self.tree.add(5)  # Попытка добавить дубликат

        # then
        self.assertEqual(self.tree.root.left.value, 5)  # Левый потомок по-прежнему 5


if __name__ == '__main__':
    unittest.main()
