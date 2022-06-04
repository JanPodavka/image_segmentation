import sys
import heapq

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

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, xroot, yroot, x, y):
    #     if rank[xroot] < rank[yroot]:
    #         parent[xroot] = yroot
    #     elif rank[xroot] > rank[yroot]:
    #         parent[yroot] = xroot
    #     else:
    #         parent[yroot] = xroot
    #         rank[xroot] += 1
        pass

    def kruskal(self, size):
        e = sorted(self.E, key=lambda x: x[2])  # sorted ascending
        L = []
        i = 0  # iterace
        root = []
        rank = []
        # for j in range(size ** 2):
        #     root.append(j)  # inicializace komponent
        #     rank.append(0)  # inicializace ranků

        for j in range(size): # pro každý Vrchol
            for k in range(size):
                root.append((j, k))  # inicializace komponent
                rank.append(0)  # inicializace ranků

        while len(L) < size ** 2 - 1:
            u, v, w = e[i]  # volba seřazené hrany
            i += 1
            r1 = self.find(u, i)
            print(r1)
            r2 = self.find(v, i)
            print(r2)
            if r1 != r2:  # pokud nejsou ve stejné komponentě -> přidej..jinak přeskoč
                #self.union(r1, r2)
                print("pass")


def parse_input(input_lines, size):
    graph = Graph(size)
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        graph.V[i] = row
    return graph


def test_file():
    with open("test_img.txt", "r", encoding="UTF8") as f:
        n = int(f.readline())
        graph = Graph(n)
        for i, line in enumerate(f.readlines()):
            row = list(map(int, line.split()))
            graph.V[i] = row
    return graph, n


if __name__ == '__main__':
    # n = int(sys.stdin.readline())  # size of img
    # lines = sys.stdin.readlines()  # lines of img
    # g = parse_input(lines, n)  # parse and make graph
    g, n = test_file()
    g.create_4_neighborhood(n)  # create 4-neigh
    g.kruskal(n)

