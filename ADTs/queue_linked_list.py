class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def is_empty(self):
        if self.first == None:
            return True

        return False

    def enqueue(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        exit = self.first
        self.first = self.first.next
        self.size -= 1
        return exit.val


def test_queue():
    q = Queue()

    assert q.is_empty() == True

    for i in range(10):
        q.enqueue(i)

    assert q.is_empty() == False

    for i in range(10):
        q.dequeue()

    print("All tests passed")


if __name__ == "__main__":
    test_queue()
