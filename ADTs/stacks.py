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

        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        pop = self.head.val
        self.head = self.head.next
        self.size -= 1
        return pop
