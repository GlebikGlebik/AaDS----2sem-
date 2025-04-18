from lab3.utils import read_input, write_output, decorate

import heapq


def build_weighted_adjacency_list(n, m, data):
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, data[i].split())
        adj[u].append((v, w))  # ориентированный граф
    return adj


def dijkstra(adj, start, end):
    n = len(adj)
    distance = [float('inf')] * n
    distance[start] = 0
    heap = [(0, start)]  # (текущая_дистанция, вершина)

    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u > distance[u]:
            continue
        if u == end:
            return dist_u
        for v, w in adj[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                heapq.heappush(heap, (distance[v], v))
    return -1 if distance[end] == float('inf') else distance[end]


def minimal_flight_cost(data):
    n, m = map(int, data[0].split())
    adj = build_weighted_adjacency_list(n, m, data[1:m+2])
    start, end = map(int, data[m+1].split())
    return dijkstra(adj, start, end)


def main():
    data = read_input(8)
    result = minimal_flight_cost(data)
    write_output(8, result)


if __name__ == '__main__':
    decorate(8, 'minimal_flight_cost')
