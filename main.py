import sys


class Graph:
    def __init__(self, size):
        self.V = [[0]*size]*size
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


if __name__ == '__main__':

    n = int(sys.stdin.readline())
    graph = Graph(n)
    lines = sys.stdin.readlines()
    for i, line in enumerate(lines):
        row = list(map(int, line.split()))
        graph.V[i] = row
        print(i)
        print(graph.V[i])


    # for i, line in enumerate(sys.stdin):
    #     row = list(map(int, line.split()))
    #     graph.V[i] = row
    #     print(i)
    #     print(graph.V[i])

    print(graph.V)
