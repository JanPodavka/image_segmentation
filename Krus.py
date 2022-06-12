from itertools import chain
import numpy as np
import sys

sys.setrecursionlimit(3000)


class Graph:
    def __init__(self, image, size):
        self.size = size
        self.values = list(chain.from_iterable(image))
        self.parent, self.E = self.getVerticles(image, size)
        self.max_values = {x: self.values[idx] for idx, x in enumerate(self.parent.values())}

    def getVerticles(self, values, size):
        V = {}
        E = []
        for i in range(size):
            for j in range(size):
                V[(i, j)] = (i, j)
                if i + 1 < size:
                    E.append([abs(values[i][j] - values[i + 1][j]), (i, j), (i + 1, j)])
                if j + 1 < size:
                    E.append([abs(values[i][j] - values[i][j + 1]), (i, j), (i, j + 1)])
                if j - 1 > -1:
                    E.append([abs(values[i][j] - values[i][j - 1]), (i, j), (i, j - 1)])
                if i - 1 > -1:
                    E.append([abs(values[i][j] - values[i-1][j]), (i, j), (i-1, j)])
        return V, E

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, u_root, v_root, w):
        self.parent[v_root] = u_root
        self.max_values[u_root] = w

    def kruskal(self):
        sorted_edges = sorted(self.E, key=lambda x: x[0])
        for weight, u, v in sorted_edges:
            u_root = self.find(u)
            v_root = self.find(v)
            treshold = min(self.max_values[u_root], self.max_values[v_root])+2
            if u_root != v_root and weight < treshold:
                self.union(u_root, v_root, weight)
        return self.get_result()

    def get_result(self):
        root_diff = self.parent
        edges = []
        for u, v in root_diff.items():
            edges.append((u[0] * self.size + u[1], v[0] * self.size + v[1]))

        background = set()
        background.add(0)
        old_b = 0
        while old_b != len(background):
            old_b = len(background)
            for tups in edges:
                if not background.isdisjoint(tups):
                    background.add(tups[0])
                    background.add(tups[1])

        result = np.array([[1] * self.size] * self.size)
        for k in range(self.size):
            for j in range(self.size):
                if k * self.size + j in background:
                    result[k][j] = 0
        return result


def read_file(path):
    with open(path, "r", encoding="UTF8") as f:
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


def write_to_file(img):
    with open("result.txt", "w") as f:
        for row in img:
            for value in row:
                f.write(str(value) + " ")
            f.write("\n")


def show_out(res):
    for row in res:
        for value in row:
            print(value, end=" ")
        print("")


if __name__ == "__main__":
    input = [['input1.txt', 'ref1.txt'], ['input3.txt', 'ref3.txt'], ['input4.txt', 'ref4.txt'],
             ['input5.txt', 'ref5.txt']]
    inputs = [['input2.txt', 'ref2.txt']]
    for file, ref in inputs:
        print(file)
        img = read_file(file)
        ref = read_file(ref)
        graph = Graph(img, img.shape[0])
        result = np.array(graph.kruskal())
        equal = np.array_equal(result, ref)
        write_to_file(result)
        print(equal)
        print("")
