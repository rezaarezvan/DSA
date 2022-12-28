class HashCell:
    def __init__(self, key,  value):
        self.key = key
        self.value = value


class HashMap:

    def __init__(self):
        self.table = [None]
        self.size = 0
        self.n_deleted = 0
        self.DELETED = HashCell(None, None)

    def load_factor(self):
        return (self.size + self.n_deleted) / len(self.table)

    def is_empty(self):
        return self.size == 0

    def add(self, key, value):
        if self.load_factor() > 0.75:
            self.resize(2 * len(self.table))

        i = hash(key) % len(self.table)

        while self.table[i] is not None and self.table[i].value != self.DELETED:
            if self.table[i].key == key:
                return
            i = (i + 1) % len(self.table)

        self.size += 1
        if self.table[i] is self.DELETED:
            self.n_deleted -= 1

        self.table[i] = HashCell(key, value)

    def contains(self, key):
        i = hash(key) % len(self.table)

        while self.table[i] is not None:
            if self.table[i].key == key:
                return True
            i = (i + 1) % len(self.table)

        return False

    def remove(self, key):
        i = hash(key) % len(self.table)

        while self.table[i] is not None:
            if self.table[i].key == key:
                self.table[i] = self.DELETED
                self.size -= 1
                self.n_deleted += 1
                if self.load_factor() < 0.25:
                    self.resize(len(self.table) // 2)
                return
            i = (i + 1) % len(self.table)

    def resize(self, new_size):
        old_table = self.table
        self.table = [None] * new_size
        self.size = 0
        self.n_deleted = 0

        for cell in old_table:
            if cell is not None and cell.value != self.DELETED:
                self.add(cell.key, cell.value)


def test_hashset():
    table = HashMap()

    assert table.is_empty()

    for i in range(100):
        table.add(i, i)

    assert not table.is_empty()

    for i in range(100):
        assert table.contains(i)

    for i in range(100):
        table.remove(i)

    assert table.is_empty()

    for i in range(100):
        assert not table.contains(i)

    print("All tests passed")


if __name__ == '__main__':
    test_hashset()
