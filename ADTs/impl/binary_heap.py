class min_priority_queue:
    '''
    A min-prio queue using (min-)binary heaps

    The heap is represented as a list, where the root is at index 0.
    The children of the node at index i are at indices 2i+1 and 2i+2.
    (or, the parent of a node is at index (i-1)//2)

    Description:
        add(item) - add an item to the heap:
            add the item to the end of the list
            if the newly added item is smaller than its parent, we swamp them
            and repeat the process until the heap property is restored

        remove_min() - remove the minimum item from the heap:
            swap the root with the last item in the list
            remove the last item from the list
            if the new root is larger than one of its children, we swap it
            with the smaller of the two children and repeat the process until
            the heap property is restored
    '''

    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def greater(self, i, j):
        return self.heap[i] > self.heap[j]

    def get_min(self):
        return self.heap[0]

    def add(self, item):
        self.heap.append(item)

        k = len(self.heap) - 1
        while k > 0 and self.greater((k - 1) // 2, k):
            self.swap((k - 1) // 2, k)
            k = (k - 1) // 2

    def remove_min(self):
        min = self.heap[0]
        n = len(self.heap) - 1
        self.swap(0, n)

        self.heap.pop()
        n -= 1

        k = 0
        while 2 * k + 1 <= n:
            j = 2 * k + 1
            if j < n and self.greater(j, j + 1):
                j += 1

            if not self.greater(k, j):
                break

            self.swap(k, j)
            k = j

        return min


def test_binary_heap():
    heap = min_priority_queue()

    for i in range(10):
        heap.add(i)

    for i in range(10):
        assert heap.remove_min() == i

    print("Test passed")


if __name__ == '__main__':
    test_binary_heap()
