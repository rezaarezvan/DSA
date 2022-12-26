# Complexities for specific data structure and algorithms

* Selection sort:
    * O(n^2)

* Insertion sort:
    * Worst-case: O(n^2)
    * O(n) for 'almost'/sorted lists.

* Merge sort:
    * O(n log n)

* Quick sort:
    * Worst-case: O(n^2)

    * Average-case: O(n log n)

    * Expected (using random pivot): O(n log n)

* Dynamic Arrays:
    * Worst-case for appending: O(n) - due to calling `resize()`

    * Amortized worst-case: O(1)

    * Looking up given index: O(1)

    * worst-case for finding a element: O(n)

    * worst-case for finding a element in sorted array: O(log n)

* Linked lists:
    * Adding element at the front: O(1)

    * Worst-case to find element or looking up an index: O(n)

* Hash tables (search, add and del items):
    * Amortized worst-caes: O(n)

    * Amortized, if the hash function is good and the input is well-behaved: O(1)

    * This is due to we're using a dynamic array behind the scences.

* BSTs (search, add and del items):
    * worst-case: O(n)

    * If the input is well-behaved: O(log n)

    * If the elements are in sorted order: O(n)

* Balanced BSTs (AVL tree, red-black tree):
    * worst-case: O(log n)

* Binary Heaps (add, rem the min/max):
    * worst-case: O(log n)

* Graph algorithms (Kurskal, Prim, UCS/Dijkstras):
    * in a **sparse** graph, O(|V|) = O(|E|), or n = |V| = |E|, O(n).

    * worst-case: O(n log n) on **sparse** graphs
