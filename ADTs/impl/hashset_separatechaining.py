class HashCell:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashSet:
    def __init__(self):
        self.table = [None]
        self.size = 0

    def add(self, value):
        if self.size >= 8 * len(self.table):
            self.resize(2 * len(self.table))

        i = hash(value) % len(self.table)

        node = self.table[i]

        while node is not None:
            if node.value == value:
                return
            node = node.next

        node = HashCell(value)
        node.next = self.table[i]
        self.table[i] = node
        self.size += 1

    def contains(self, value):
        i = hash(value) % len(self.table)

        node = self.table[i]

        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False

    def remove(self, value):
        if self.size <= 2 * len(self.table):
            if len(self.table) // 2 <= 0:
                self.resize(1)
            else:
                self.resize(len(self.table) // 2)

        i = hash(value) % len(self.table)

        node = self.table[i]
        prev = None

        while node is not None:
            if node.value == value:
                if prev is None:
                    self.table[i] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return
            prev = node
            node = node.next

    def resize(self, new_size):
        new_table = [None] * new_size

        for node in self.table:
            while node is not None:
                i = hash(node.value) % new_size

                next = node.next

                node.next = new_table[i]
                new_table[i] = node

                node = next

        self.table = new_table

    def is_empty(self):
        return self.size == 0


def test_hashset():
    hashset = HashSet()

    assert hashset.is_empty()

    for i in range(100):
        hashset.add(i)

    assert not hashset.is_empty()

    for i in range(100):
        assert hashset.contains(i)

    for i in range(100):
        hashset.remove(i)

    assert hashset.is_empty()

    print("All tests passed!")


if __name__ == "__main__":
    test_hashset()
