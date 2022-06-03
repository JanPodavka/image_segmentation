import sys


class Graph:
    def __init__(self, size):
        self.V = [[0] * size] * size
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


def parse_input(input_lines, size):
    graph = Graph(size)
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        graph.V[i] = row
    return graph


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    g = parse_input(lines, n)
    print(g.V)

