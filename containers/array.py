class Array(object):
    def __init__(self):
        self.values = [None]
        self.size = 0

    def append(self, value):
        if self.size == len(self.values):
            self.resize(len(self.values) * 2)

        self.values[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('pop from empty {}'.format(self.__class__.__name__))

        self.size -= 1
        value = self.values[self.size]
        self.values[self.size] = None

        if self.size == len(self.values) // 4:
            self.resize(len(self.values) // 2)

        return value

    def resize(self, size):
        values = [None] * size

        for i in range(self.size):
            values[i] = self.values[i]

        self.values = values

    def __getitem__(self, i):
        if i not in range(self.size):
            raise IndexError('array index out of range')

        return self.values[i]

    def __setitem__(self, i, value):
        if i not in range(self.size):
            raise IndexError('array index out of range')

        self.values[i] = value

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(self.size - 1, -1, -1):
            yield self.values[i]
