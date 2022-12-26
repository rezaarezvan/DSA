# Complexities for specific data structure and algorithms

* Selection sort:
    * $\mathcal{O}(n^2)$

* Insertion sort:
    * Worst-case: $\mathcal{O}(n^2)$
    * $\mathcal{O}(n)$ for 'almost'/sorted lists.

* Merge sort:
    * $\mathcal{O}(n\ log(n))$

* Quick sort:
    * Worst-case: $\mathcal{O}(n^2)$

    * Average-case: $\mathcal{O}(n\ log(n))$

    * Expected (using random pivot): $\mathcal{O}(n\ log(n))$

* Dynamic Arrays:
    * Worst-case for appending: $\mathcal{O}(n)$ - due to calling `resize()`

    * Amortized worst-case: $\mathcal{O}(1)$

    * Looking up given index: $\mathcal{O}(1)$

    * worst-case for finding a element: $\mathcal{O}(n)$

    * worst-case for finding a element in sorted array: $\mathcal{O}(log(n))$

* Linked lists:
    * Adding element at the front: $\mathcal{O}(1)$

    * Worst-case to find element or looking up an index: $\mathcal{O}(n)$

* Hash tables (search, add and del items):
    * Amortized worst-caes: $\mathcal{O}(n)$

    * Amortized, if the hash function is good and the input is well-behaved: $\mathcal{O}(1)$

    * This is due to we're using a dynamic array behind the scences.

* BSTs (search, add and del items):
    * worst-case: $\mathcal{O}(n)$

    * If the input is well-behaved: $\mathcal{O}(log(n))$

    * If the elements are in sorted order: $\mathcal{O}(n)$

* Balanced BSTs (AVL tree, red-black tree):
    * worst-case: $\mathcal{O}(log(n)$

* Binary Heaps (add, rem the min/max):
    * worst-case: $\mathcal{O}(log(n))$

* Graph algorithms (Kurskal, Prim, UCS/Dijkstras):
    * in a **sparse** graph, $\mathcal{O}(|V|) = O(|E|), \text{ or } n  = |V| = |E|, O(n)$.

    * worst-case: $\mathcal{O}(n\ log(n))$ on **sparse** graphs
