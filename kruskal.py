from itertools import chain
import numpy as np
import sys


class Graph:
    def __init__(self, image, size):
        self.size = size
        self.parent, self.E = self.getVerticles(image, size)
        self.num_of_components = size ** 2
        self.rank = {x: 0 for x in self.parent.values()}

    def getVerticles(self, values, size):
        parent = {}
        E = []
        for i in range(size):
            for j in range(size):
                parent[(i, j)] = (i, j)
                if i + 1 < size:
                    E.append([abs(values[i][j] - values[i + 1][j]), (i, j), (i + 1, j)])
                if j + 1 < size:
                    E.append([abs(values[i][j] - values[i][j + 1]), (i, j), (i, j + 1)])
        return parent, E

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, u_root, v_root):
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        self.num_of_components -= 1

    def kruskal(self):
        sorted_edges = sorted(self.E, key=lambda x: x[0])
        for weight, u, v in sorted_edges:
            u_root = self.find(u)
            v_root = self.find(v)
            if self.num_of_components == 2:
                break
            if u_root != v_root:
                self.union(u_root, v_root)
        self.get_results()

    def get_results(self):
        bg_root = self.find((0, 0))
        for i in range(self.size):
            for j in range(self.size):
                curr_root = self.find((i, j))
                if curr_root == bg_root:
                    print(0, end=" ")
                else:
                    print(1, end=" ")
            print("")


def parse_input(input_lines, size):
    values = [[0] * size] * size
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        values[i] = row
    return np.array(values)


if __name__ == "__main__":
    n = int(sys.stdin.readline())  # size of img
    lines = sys.stdin.readlines()  # lines of img
    img = parse_input(lines, n)  # parse and make graph
    graph = Graph(img, img.shape[0])
    graph.kruskal()
