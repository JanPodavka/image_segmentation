import sys


class Graph:
    def __init__(self, size):
        self.V = [[0]*size]*size
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    graph = Graph(n)
    for i, line in enumerate(sys.stdin):
        row = list(map(int, line.split()))
        for j, v in enumerate(row):
            graph.V[i][j] = v

    print(graph.V)
