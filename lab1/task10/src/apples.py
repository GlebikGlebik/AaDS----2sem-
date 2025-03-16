import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))
from lab1.utils import read_input, write_output, decorate


class ApplesSolver:
    def __init__(self, task, input_data=None):
        self.task = task
        if input_data is not None:
            self.input_data = input_data
        else:
            self.input_data = read_input(task)

        # Парсим n и s из первой строки входных данных
        self.n, self.s = map(int, self.input_data[0].split())
        apples = [tuple(map(int, line.split())) for line in self.input_data[1:self.n + 1]]

        # Разделяем яблоки на группы
        self.group_a = []  # b_i > a_i (увеличивают рост)
        self.group_b = []  # b_i <= a_i (уменьшают рост)
        for idx, (a, b) in enumerate(apples, 1):
            if b > a:
                self.group_a.append((a, b, idx))
            else:
                self.group_b.append((a, b, idx))

        # Сортируем группу A по возрастанию a_i
        self.group_a.sort(key=lambda x: x[0])
        # Сортируем группу B по убыванию b_i
        self.group_b.sort(key=lambda x: -x[1])

    def solve(self):
        current_height = self.s
        order = []
        # Обрабатываем группу A
        for a, b, idx in self.group_a:
            if current_height - a <= 0:
                return -1
            current_height = current_height - a + b
            order.append(idx)
        # Обрабатываем группу B
        for a, b, idx in self.group_b:
            if current_height - a <= 0:
                return -1
            current_height = current_height - a + b
            order.append(idx)
        return order

    def save_result(self, result):
        if result == -1:
            write_output(self.task, -1)
        else:
            write_output(self.task, ' '.join(map(str, result)))


def main():
    task = 10
    solver = ApplesSolver(task)
    result = solver.solve()
    solver.save_result(result)


if __name__ == "__main__":
    main()

