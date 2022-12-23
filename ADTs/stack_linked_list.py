class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True

        return False

    def push(self, val):
        if self.head == None:
            self.head = Node(val)
            return

        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self):
        if self.head == None:
            return None

        pop = self.head.val
        self.head = self.head.next
        self.size -= 1
        return pop


def test_stack():
    stack = Stack()

    assert stack.is_empty() == True

    for i in range(10):
        stack.push(i)

    assert stack.is_empty() == False

    for i in range(10):
        assert stack.pop() == 9 - i

    assert stack.is_empty() == True

    assert stack.pop() == None

    print("All tests passed!")


if __name__ == "__main__":
    test_stack()
