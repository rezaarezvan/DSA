```
DirectedGraph<Node>:

    /*
    A directed graph is a graph (vertices and edges) where each edge has a weight.

    These weights can represent, wait-times, 'cost' etc.
    */

    // Adds an edge to the graph
    void add(DirectedEdge<Node> e)

    // Removes an edge from the graph
    void remove(DirectedEdge<Node> e)

    // Returns True if the graph contains the edge, False otherwise
    boolean contains(DirectedEdge<Node> e)

    // Returns all edges that goes out from Node, n
    Collection<DirectedEdge<Node>>
        outgoing_edges(Node n)

    // Returns the total number of nodes in the graph
    int n_node()

    // Returns the total number of edges in the graph
    int n_edges()
```
