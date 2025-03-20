import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))
from lab2.utils import read_input, write_output


class TreeHeightSolver:
    def __init__(self, task, input_data=None):
        self.task = task
        if input_data is not None:
            self.input_data = input_data
        else:
            self.input_data = read_input(task)

        # Парсим входные данные
        self.n = int(self.input_data[0])
        self.nodes = [(0, 0)] * (self.n + 1)  # Индексация с 1 до n
        self.all_nodes = set(range(1, self.n + 1))

        for i in range(1, self.n + 1):
            parts = self.input_data[i].split()
            k = int(parts[0])
            l = int(parts[1])
            r = int(parts[2])
            self.nodes[i] = (l, r)
            if l != 0:
                self.all_nodes.discard(l)
            if r != 0:
                self.all_nodes.discard(r)

        # Корень дерева
        self.root = self.all_nodes.pop() if self.all_nodes else 0

    def solve(self):
        if self.n == 0:
            return 0

        max_depth = 0
        stack = [(self.root, 1)]

        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            left, right = self.nodes[node]
            if left != 0:
                stack.append((left, depth + 1))
            if right != 0:
                stack.append((right, depth + 1))

        return max_depth

    def save_result(self, result):
        write_output(self.task, result)


def main():
    task = 8  # Номер задачи
    solver = TreeHeightSolver(task)
    result = solver.solve()
    solver.save_result(result)


if __name__ == "__main__":
    main()