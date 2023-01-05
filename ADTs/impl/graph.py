import random
from queue import PriorityQueue
import queue_linked_list


class Edge:
    '''
    Auxilary Edge class for the Graph class.
    '''

    def __init__(self, src, dst, weight=1):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return f'{self.src} -> {self.dst} ({self.weight})'


class Graph:
    '''
    A class that represents a directed graph using adjacency list representation

    Attributes:
        graph (dict): A dictionary representing the graph as adjacency list
        n_edges (int): Number of edges in the graph
        all_vertices (set): A set of all vertices in the graph

    Description:
        outgoing_edges(v) returns a list of all edges that have v as their source
        add(edge) adds an edge to the graph
        remove(edge) removes an edge from the graph

        recursive_dfs(v, visited) performs a recursive depth first search on the graph

        Note: DFS (Depth First Search) is an algorithm for traversing a Graph

        It goes as deep as possible (visits all the children of a node)
        before before backtracking to the parent node and visiting the next child.

        iterative_BFS(v) performs an iterative breadth first search on the graph

        Note: BFS (Breadth First Search) is an algorithm for traversing a Graph

        It visits all the nodes at a given level before going to the next level.
        (If we think of the graph as a tree)

        In a arbitrary graph, the BFS uses a queue to keep track of the nodes to visit.
        The queue is initialized with the starting node.
        The algorithm then visits the first node in the queue, enqueues all of its children to the queue
        and then dequeues the first node from the queue. This process is repeated until the queue is empty.


        UCS(self, start) performs a uniform cost search on the graph

        Note: Uniform Cost Search is an algorithm for traversing a graph

        It is similar to BFS, but instead of using a queue, it uses a priority queue_linked_list
        The priority queue_linked_list is initialized with the starting node and its cost.


    '''

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

    def iterative_BFS(self, start):
        visited = set()
        q = queue_linked_list.Queue()
        q.enqueue(start)
        visited.add(start)

        while not q.is_empty():
            v = q.dequeue()
            print(f'Visited {v}')

            for edge in self.outgoing_edges(v):
                w = edge.dst
                if w not in visited:
                    q.enqueue(w)
                    visited.add(w)

    def UCS(self, start):
        visited = set()
        q = PriorityQueue()
        q.put((0, start))
        visited.add((0, start))

        while not q.empty():
            cost, v = q.get()
            print(f'Visited {(cost, v)}')

            for edge in self.outgoing_edges(v):
                w = edge.dst
                if (cost+edge.weight, w) not in visited:
                    q.put((cost+edge.weight, w))
                    visited.add((cost+edge.weight, w))


def test_graph():
    g = Graph()

    for i in range(10):
        g.add(Edge(random.randint(1, 10), random.randint(0, 10)))

    g.add(Edge(1, 2))
    g.add(Edge(1, 3))
    g.add(Edge(1, 4))

    print(g)

    print("\nDFS from 1")
    g.recursive_DFS(1, set())

    print("\nBFS from 1")
    g.iterative_BFS(1)

    print("\nUCS from 1")
    g.UCS(1)

    print("All tests passed")


if __name__ == "__main__":
    test_graph()
