class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    '''
    A stack implementation using linked lists.

    Using a pointer node - we keep track of the stack-top.

    Complexity:

        is_empty():
            O(1)

        push():
            O(1)

        pop():
            O(1)
    '''

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)

        else:
            new = Node(val)
            new.next = self.head
            self.head = new
            self.size += 1

    def pop(self):
        if self.head is None:
            return None

        pop = self.head.val
        self.head = self.head.next
        self.size -= 1
        return pop


def test_stack():
    stack = Stack()

    assert stack.is_empty() is True

    for i in range(10):
        stack.push(i)

    assert stack.is_empty() is False

    for i in range(10):
        assert stack.pop() is 9 - i

    assert stack.is_empty() is True

    assert stack.pop() is None

    print("All tests passed!")


if __name__ == "__main__":
    test_stack()
