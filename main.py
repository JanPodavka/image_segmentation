import sys


class Graph:
    def __init__(self, size):
        self.V = [[0] * size] * size
        self.E = []

    def add_edge(self, x, y, w):
        self.E.append([x, y, w])

    def create_4_neighborhood(self, size):
        for i in range(0, size):
            for j in range(0, size):  # vždy přidat hranu pod a po pravé straně, pokud je to možné
                if i + 1 < size:
                    self.add_edge((i, j), (i + 1, j), abs(self.V[i][j] - self.V[i + 1][j]))
                if j + 1 < size:
                    self.add_edge((i, j), (i, j + 1), abs(self.V[i][j] - self.V[i][j + 1]))

    # Union-Find ##

    def find(self, x):
        print("s")

    def union(self, u, v):
        print("s")

    def kruskal(self, size):
        e = sorted(self.E, key=lambda x: x[2])  # sorted ascending
        L1 = []
        i = 0  # iterace

        root = []
        rank = []
        for node in range(size ** 2):
            root.append(node)  # inicializace komponent
            rank.append(0)  # inicializace ranků

        while len(L1) < size ** 2 - 1:
            u, v, w = e[i] # volba seřazené hrany
            i += 1
            if self.find(u) != self.find(v):  # pokud nejsou ve stejné komponentě -> přidej..jinak přeskoč
                self.union(self.find(u), self.find(v))


def parse_input(input_lines, size):
    graph = Graph(size)
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        graph.V[i] = row
    return graph


if __name__ == '__main__':
    n = int(sys.stdin.readline())  # size of img
    lines = sys.stdin.readlines()  # lines of img
    g = parse_input(lines, n)  # parse and make graph
    g.create_4_neighborhood(n)  # create 4-neigh
    g.kruskal(n)
