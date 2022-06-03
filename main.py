import sys


class Graph:
    def __init__(self, size):
        self.V = [[0] * size] * size
        self.graph = []

    def add_edge(self, x, y, w):
        self.graph.append([x, y, w])

    def create_4_neighborhood(self, size):
        for i in range(0, size):
            for j in range(0, size): # vždy přidat hranu pod a po levé straně, pokud je to možné
                if i + 1 < size:
                    self.add_edge((i, j), (i + 1, j), abs(self.V[i][j] - self.V[i + 1][j]))
                if j + 1 < size:
                    self.add_edge((i, j), (i, j + 1), abs(self.V[i][j] - self.V[i][j+1]))

    def kruskal(self):
        pass

def parse_input(input_lines, size):
    graph = Graph(size)
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        graph.V[i] = row
    return graph


if __name__ == '__main__':
    n = int(sys.stdin.readline()) # size of img
    lines = sys.stdin.readlines() # lines of img
    g = parse_input(lines, n) # parse and make graph
    g.create_4_neighborhood(n) # create 4-neigh

