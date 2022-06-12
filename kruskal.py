import sys
from itertools import chain
import numpy as np


class Graph:
    def __init__(self, image, size):
        self.size = size
        self.values = list(chain.from_iterable(image))
        self.V, self.E = self.getVerticles(image, size)
        self.parent = {x: x for x in self.V}
        self.rank = {x: 0 for x in self.V}
        self.max_values = {x: self.values[idx] for idx, x in enumerate(self.V)}

    def getVerticles(self, values, size):
        V = []
        E = []
        for i in range(size):
            for j in range(size):
                V.append((i, j))
                if i + 1 < size:
                    E.append([abs(values[i][j] - values[i + 1][j]), (i, j), (i + 1, j)])
                if j + 1 < size:
                    E.append([abs(values[i][j] - values[i][j + 1]), (i, j), (i, j + 1)])
        return V, E

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, u_root, v_root, w):
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
            self.max_values[u_root] = w
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
            self.max_values[v_root] = w
        else:
            self.parent[v_root] = u_root
            self.max_values[v_root] = w
            self.rank[v_root] += 1  # a0

    def kruskal(self):

        sorted_edges = sorted(self.E, key=lambda x: x[0])
        for weight, u, v in sorted_edges:
            u_root = self.find(u)
            v_root = self.find(v)
            if u_root != v_root and weight < 2:
                self.union(u_root, v_root, weight)

        bg_root = self.find((0, 0))
        for i in range(self.size):
            for j in range(self.size):
                curr_root = self.find((i, j))
                if curr_root == bg_root:
                    print(0, end=" ")
                else:
                    print(1, end=" ")
            print("")


def read_file():
    with open("input3.txt", "r", encoding="UTF8") as f:
        n = int(f.readline())
        values = [[0] * n] * n
        for i, line in enumerate(f.readlines()):
            values[i] = list(map(int, line.split()))
    return np.array(values)


def parse_input(input_lines, size):
    values = [[0] * size] * size
    for i, line in enumerate(input_lines):
        row = list(map(int, line.split()))
        values[i] = row
    return np.array(values)


def show_out(res):
    for row in res:
        for value in row:
            print(value, end=" ")
        print("")


if __name__ == "__main__":
    # n = int(sys.stdin.readline())  # size of img
    # lines = sys.stdin.readlines()  # lines of img
    # img = parse_input(lines, n)  # parse and make graph
    img = read_file()
    graph = Graph(img, img.shape[0])
    graph.kruskal()
    #show_out(result.tolist())
