import sys
import os

from lab3.utils import read_input, write_output

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Labyrinth:
    def __init__(self):
        self.input_file = read_input(2)
        self.graph = {}
        self.n, self.m = map(int, self.input_file[0].split())

        for i in range(1, self.n + 1):
            self.graph.setdefault(i, set())

    def graph_builder(self):
        for j in self.input_file[1:]:
            start, end = map(int, j.split())
            self.graph[start].add(end)
            self.graph[end].add(start)
        return self.graph

    def components_counter(self):
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in self.graph[node]:
                dfs(neighbor)

        count = 0
        for i in self.graph.keys():
            if i not in visited:
                dfs(i)
                count += 1

        return count

    def resulting_function(self):
        self.graph_builder()
        return self.components_counter()


def main():
    lab = Labyrinth()
    res = lab.resulting_function()
    write_output(2, res)

if __name__ == '__main__':
    main()
