class Queue:
    def __init__(self):
        self.queue = [None]
        self.head = 0
        self.tail = 1

    def is_empty(self):
        return self.head == (self.tail + 1) % len(self.queue)

    def enqueue(self, val):
        if (self.tail + 1) % len(self.queue) == self.head:
            self.resize(2 * len(self.queue))

        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % len(self.queue)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        result = self.queue[self.head]
        self.head = (self.head + 1) % len(self.queue)

        return result

    def resize(self, new_size):
        old_queue = self.queue
        self.queue = [None] * new_size

        if self.head < self.tail:
            for i in range(self.tail - self.head):
                self.queue[i] = old_queue[(self.head + i) % len(old_queue)]

            self.head = 0
            self.tail = self.tail - self.head

        else:
            for i in range(len(old_queue) - 1):
                _index = (self.head + i) % len(old_queue)
                self.queue[i] = old_queue[_index]

            self.head = 0
            self.tail = self.tail - self.head - 1


def test_queue():
    q = Queue()

    assert q.is_empty() == True

    for i in range(10):
        q.enqueue(i)

    assert q.is_empty() == False

    for i in range(10):
        q.dequeue()

    assert q.is_empty() == True

    print("All tests passed")


if __name__ == "__main__":
    test_queue()
