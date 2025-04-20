import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class Labyrinth:
    def __init__(self):
        self.input_file = read_input(1)
        self.graph = {}
        self.n, self.m = map(int, self.input_file[0].split())
        self.start, self.end = map(int, self.input_file[-1].split())

        for i in range(1, self.n + 1):
            self.graph.setdefault(i, set())

    def graph_builder(self):
        for j in self.input_file[1:-1]:
            start, end = map(int, j.split())
            if start not in self.graph:
                self.graph[start] = set()
            if end not in self.graph:
                self.graph[end] = set()
            self.graph[start].add(end)
            self.graph[end].add(start)
        return self.graph

    def path_finder(self):
        for i in self.graph[self.start]:
            if i == self.end:
                return 1
        return 0

    def resulting_function(self):
        self.graph_builder()
        return self.path_finder()


def main():
    lab = Labyrinth()
    res = lab.resulting_function()
    write_output(1, res)


if __name__ == '__main__':
    main()
