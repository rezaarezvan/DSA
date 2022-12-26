class Stack:
    '''
    A stack implementation using dynamic arrays.
    We use the last item in the array as the stack-head.
    This so we can achieve O(1) complexity on all stack operations.

    Complexity:

        is_empty()
            O(1)

        push():
            Best/Average-case:
                O(1)
            Worst-case:
                O(n) - due to calling resize()

        pop():
            Best/Average-case:
                O(1)
            Worst-case:
                O(n) - due to calling resize()
        resize():
            O(n)
    '''

    def __init__(self):
        self.stack = [None]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, val):
        if self.size == len(self.stack):
            self.resize(2 * self.size)

        self.stack[self.size] = val
        self.size += 1

    def pop(self):
        self.size -= 1
        pop = self.stack[self.size]
        self.stack[self.size] = None
        if self.size == (len(self.stack) // 4):
            self.resize(len(self.stack) // 2)

        return pop

    def resize(self, factor):
        new_array = [None] * factor

        for i in range(self.size):
            new_array[i] = self.stack[i]

        self.stack = new_array


def test_stack():
    stack = Stack()

    assert stack.is_empty() is True

    for i in range(10):
        stack.push(i)

    assert stack.is_empty() is False

    for i in range(10):
        assert stack.pop() == 9 - i

    assert stack.is_empty() is True

    print("All tests passed")


if __name__ == "__main__":
    test_stack()
