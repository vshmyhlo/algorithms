# TODO: use array
class PriorityQueue(object):
    def __init__(self):
        self.values = [None]

    def push(self, value):
        self.values.append(value)
        self.swim(len(self.values) - 1)

    def pop_max(self):
        if len(self.values) == 1:
            raise IndexError('pop from empty {}'.format(self.__class__.__name__))

        value = self.values[1]
        self.values[1] = self.values[-1]
        self.values.pop()
        self.sink(1)

        return value

    def swim(self, i):
        while i >= 2:
            j = i // 2
            if self.values[j] < self.values[i]:
                self.values[j], self.values[i] = self.values[i], self.values[j]

            i = j

    def sink(self, i):
        while i * 2 < len(self.values):
            j = i * 2

            if j + 1 < len(self.values) and self.values[j] < self.values[j + 1]:
                j += 1

            if self.values[i] < self.values[j]:
                self.values[i], self.values[j] = self.values[j], self.values[i]
            else:
                break

            i = j

    def __len__(self):
        return len(self.values) - 1
