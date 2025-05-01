import sys
import os
from sys import setrecursionlimit

from lab3.utils import read_input, write_output

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

setrecursionlimit(3000)


class Labyrinth:
    def __init__(self):
        self.input_file = read_input(3)
        self.graph = {}
        self.n, self.m = map(int, self.input_file[0].split())
        self.visited = set()
        self.stack = set()

        for i in range(1, self.n + 1):
            self.graph.setdefault(i, [])

    def graph_builder(self):
        for i in range(1, self.n + 1):
            self.graph[i] = []

        for j in self.input_file[1:]:
            start, end = map(int, j.split())
            self.graph[start].append(end)

        return self.graph

    def dfc(self, node):
        if node in self.stack:
            return True

        if node in self.visited:
            return False

        self.visited.add(node)
        self.stack.add(node)

        for neighbour in self.graph[node]:
            if self.dfc(neighbour):
                return True

        self.stack.remove(node)
        return False

    def cycles_finder(self):
        for i in self.graph.keys():
            if i not in self.visited:
                if self.dfc(i):
                    return 1
        return 0

    def resulting_function(self):
        self.graph_builder()
        return self.cycles_finder()


def main():
    lab = Labyrinth()
    res = lab.resulting_function()
    write_output(3, res)


if __name__ == '__main__':
    main()
