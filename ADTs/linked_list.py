class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val=None):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True

        return False

    def append(self, val):
        if self.head == None:
            self.head = Node(val)
            return

        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.next = Node(val)
        self.size += 1

    def remove_last(self):
        if self.head == None:
            return None

        curr_node = self.head
        while curr_node.next.next != None:
            curr_node = curr_node.next

        curr_node.next = None
        self.size -= 1
        return

    def remove_first(self):
        if self.head == None:
            return None

        self.head = self.head.next
        self.size -= 1
        return

    def remove(self, val):
        if self.head == None:
            return None

        curr_node = self.head

        while curr_node.next.val != val:
            curr_node = curr_node.next

        if curr_node.next.next == None:
            self.remove_last()
            return

        curr_node.next = curr_node.next.next
        self.size -= 1
        return


def test_linked_list():
    ll = LinkedList()
    assert ll.is_empty() == True

    for i in range(10):
        ll.append(i)

    assert ll.is_empty() == False
    assert ll.size == 9

    curr_node = ll.head
    for i in range(ll.size):
        assert curr_node.val == i
        curr_node = curr_node.next

    ll.remove(5)
    assert ll.size == 8

    for i in range(ll.size):
        ll.remove_last()

    assert ll.size == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_linked_list()
