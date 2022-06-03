import sys


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for line in sys.stdin:
        line_1 = list(map(int, line.split()))

