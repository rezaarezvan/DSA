'''
A program to represent graphs in python
'''


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
        return self.all_edges.get(v)

    def add(self, edge: Edge):
        if edge.src == edge.dst:
            return

        if edge not in self.all_edges:
            self.all_edges[edge.src] = edge
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


def test_graph():
    g = Graph()

    for i in range(1, 5):
        g.add(Edge(i, i+1))

    print(g)

    for i in range(1, 5):
        g.remove(Edge(i, i+1))

    print(g)

    print("All tests passed")


if __name__ == "__main__":
    test_graph()
