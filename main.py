import sys


class Graph:
    def __init__(self, size):
        self.V = [[0] * size] * size
        self.graph = []

    def add_edge(self, x, y, w):
        self.graph.append([x, y, w])

    def create_4_neighborhood(self, size):
        for i in range(0, size):
            for j in range(0, size):
                print(i, j)
                if i + 1 < size:
                    self.add_edge((i, j), (i + 1, j), abs(self.V[i][j] - self.V[i + 1][j]))
                if j + 1 < size:
                    self.add_edge((i, j), (i, j + 1), abs(self.V[i][j] - self.V[i][j+1]))
            print(len(g.graph))


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
    g.create_4_neighborhood(n)
    print(g.graph)
