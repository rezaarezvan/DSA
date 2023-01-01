class min_priority_queue:
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
