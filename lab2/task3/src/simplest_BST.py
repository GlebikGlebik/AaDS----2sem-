import sys
import os

from lab2.utils import read_input, write_output, decorate

sys.setrecursionlimit(3100)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None  # Ссылка на левого потомка
        self.right = None  # Ссылка на правого потомка

class BinaryTree:
    def __init__(self):
        self.root = None  # Корень дерева

    def add(self, value):
        if self.root is None:
            self.root = Node(value)  # Если дерево пустое, создаем корень
        else:
            self.add_recursively(self.root, value)  # Вставляем рекурсивно

    def add_recursively(self, node, value):
        # Если значение меньше текущего узла, идем в левое поддерево
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Создаем нового узла
            else:
                self.add_recursively(node.left, value)  # Рекурсивный вызов
        else:  # Если значение больше или равно, идем в правое поддерево
            if node.right is None:
                node.right = Node(value)  # Создаем нового узла
            else:
                self.add_recursively(node.right, value)  # Рекурсивный вызов

    def find_min_greater_than(self, value):
        result = self.find_min_greater_than_processing(self.root, value)
        return result if result is not None else '0'  # Возвращаем '0', если результат None

    def find_min_greater_than_processing(self, node, value):
        if node is None:
            return None  # Если узел пустой, возвращаем None

        # Если текущее значение больше, чем искомое, ищем в левом поддереве
        if node.value > value:
            left_result = self.find_min_greater_than_processing(node.left, value)
            return node.value if left_result is None else left_result
        else:
            # Иначе ищем в правом поддереве
            return self.find_min_greater_than_processing(node.right, value)

# Пример использования
def main():
    tree = BinaryTree()
    res = ''''''
    input_file = read_input(3)
    for i in range(len(input_file)):
        operation, value = input_file[i].split()
        value = int(value)  # Преобразуем значение в int
        if operation == '+':
            tree.add(value)
        elif operation == '>':
            result = tree.find_min_greater_than(value)
            res += str(result) + '\n'  # Добавляем результат в строку

    write_output(3, res)

if __name__ == '__main__':
    main()
