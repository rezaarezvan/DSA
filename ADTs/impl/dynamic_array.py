class dynamic_array:
    '''
    A dynamic array which resizes accordingly.

    Contains a size variable so we don't need to call a function which would take O(n) time to find the length.

    Complexity:

        get():
            O(1)

        set():
            O(1)

        append():
            Best-case/Average:
                O(1)
            Worst-case:
                O(n) - due to calling resize()

        resize():
            O(n)
    '''

    def __init__(self):
        self.array = [None]
        self.size = 0

    def get(self, i):
        assert 0 <= i < self.size
        return self.array[i]

    def set(self, i, val):
        assert 0 <= i < self.size
        self.array[i] = val

    def append(self, val):
        if self.size == len(self.array):
            self.resize()

        self.array[self.size] = val
        self.size += 1

    def resize(self):
        growth_factor = 2 * self.size
        new_array = [None] * growth_factor

        for i in range(len(self.array)):
            new_array[i] = self.array[i]

        self.array = new_array

    '''
    def remove(self, index):
        if self.size == 0:
            return "Error, array is empty"

        if 0 < index < self.size:
            return "Error, index out of bounds"

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1
    '''


def test_dynamic_array():
    test_array = dynamic_array()
    for i in range(10):
        test_array.append(i)

    for i in range(10):
        assert test_array.get(i) == i

    for i in range(10):
        test_array.set(i, i * 2)

    for i in range(10):
        assert test_array.get(i) == i * 2

    print("All tests passed")


if __name__ == "__main__":
    test_dynamic_array()
