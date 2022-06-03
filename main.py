import sys


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


if __name__ == '__main__':
    n = None
    for line in sys.stdin:
        if n is None:
            n = line
        else:
            print(line)
