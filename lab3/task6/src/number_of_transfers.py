from lab3.utils import read_input, write_output, decorate

from collections import deque


def build_adjacency_list(n, m, data):
    adj = [[] for _ in range(n + 1)]
    for index in range(m):
        u, v = map(int, data[index].split())
        adj[u].append(v)
        adj[v].append(u)
        index += 1
    return adj


def find_shortest_path(adj, start, end):
    distance = [-1] * (len(adj))
    distance[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in adj[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                if neighbor == end:
                    return distance[neighbor]
                queue.append(neighbor)
    return -1


def number_of_transfers(data):
    n, m = map(int, data[0].split())

    adj = build_adjacency_list(n, m, data[1:m + 2])

    start, end = map(int, data[-1].split())

    result = find_shortest_path(adj, start, end)
    return result


def main():
    data = read_input(6)
    result = number_of_transfers(data)
    write_output(6, result)


if __name__ == '__main__':
    decorate(6, 'number_of_transfers')
