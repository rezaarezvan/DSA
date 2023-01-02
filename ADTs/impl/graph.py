'''
A program to represent graphs in python
'''


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, src: Vertex, dst: Vertex, weight=1):
        self.src = src
        self.dst = dst
        self.weight = weight


class Graph:
    def __init__(self):
        self.all_edges = {}
        self.n_edges = 0
        self.all_vertices = set()

    def outgoing_edges(self, v: Vertex):
        return self.all_edges.get(v)

    def add(self, edge: Edge):
        if edge not in self.all_edges:
            self.all_edges[edge.src] = edge
            self.n_edges += 1
            self.all_vertices.add(edge.src)
            self.all_vertices.add(edge.dst)

    def remove(self, edge: Edge):
        if edge in self.all_edges:
            self.all_edges.pop(edge)
            self.n_edges -= 1


def test_graph():
    g = Graph()


if __name__ == "__main__":
    test_graph()
