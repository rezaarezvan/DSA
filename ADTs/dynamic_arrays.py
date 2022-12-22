class dynamic_array:
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
        new_array = [None] * 2

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
