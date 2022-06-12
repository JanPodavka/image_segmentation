import sys
import time
from itertools import chain
import numpy as np
import setuptools.command.alias


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

        return self.get_result()

    def get_result(self):

        root_diff = self.parent
        edges = []
        object = set()
        for u, v in root_diff.items():
            edges.append((u[0] * self.size + u[1], v[0] * self.size + v[1]))
            object.add(u[0] * self.size + u[1])
            object.add(v[0] * self.size + v[1])



        #object = set(edges)

        # background = set()
        # background.add(0)
        # while not background.isdisjoint(object):
        #     for tups in edges:
        #         if not background.isdisjoint(tups):
        #             background.add(tups[0])
        #             background.add(tups[1])
        #             edges.remove(tups)
        #             object.discard(tups[0])
        #             object.discard(tups[1])
        background = set()
        background.add(0)
        old_o = 0
        old_b = 0
        while old_o != len(object) and old_b != len(background):
            old_b = len(background)
            old_o = len(object)
            for tups in edges:
                if not background.isdisjoint(tups):
                    background.add(tups[0])
                    background.add(tups[1])
                    object.discard(tups[0])
                    object.discard(tups[1])



        result = np.array([[1] * self.size] * self.size)
        for i in range(self.size):
            for j in range(self.size):
                if i * self.size + j in background:
                    result[i][j] = 0
        return result


def read_file():
    with open("input1.txt", "r", encoding="UTF8") as f:
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
    result = graph.kruskal()
    show_out(result.tolist())

