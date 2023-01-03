'''
A program to represent graphs in python
'''

import random


class Edge:
    def __init__(self, src, dst, weight=1):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return f'{self.src} -> {self.dst} ({self.weight})'


class Graph:
    def __init__(self):
        self.all_edges = {}
        self.n_edges = 0
        self.all_vertices = set()

    def outgoing_edges(self, v):
        tmp = []
        for edge in self.all_edges.values():
            if edge.src == v:
                tmp.append(edge)

        return tmp

    def add(self, edge: Edge):
        if edge.src == edge.dst:
            return

        self.all_edges[(edge.src, edge.dst)] = edge
        self.n_edges += 1
        self.all_vertices.add(edge.src)
        self.all_vertices.add(edge.dst)

    def remove(self, edge: Edge):
        if edge.src in self.all_edges:
            del self.all_edges[edge.src]
            self.n_edges -= 1

    def __str__(self):
        print(
            f'Number of edges: {self.n_edges} and vertices: {self.all_vertices}')
        for edge in self.all_edges.values():
            print(edge)
        return ''

    def recursive_DFS(self, start, visited):
        visited.add(start)
        print(f'Visited {start}')

        for edge in self.outgoing_edges(start):
            w = edge.dst
            if w not in visited:
                self.recursive_DFS(w, visited)


def test_graph():
    g = Graph()

    for i in range(10):
        g.add(Edge(random.randint(1, 10), random.randint(0, 10)))

    g.add(Edge(1, 2))
    g.add(Edge(1, 3))
    g.add(Edge(1, 4))

    print(g)
    g.recursive_DFS(1, set())

    print("All tests passed")


if __name__ == "__main__":
    test_graph()
