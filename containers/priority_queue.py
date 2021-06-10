from containers.array import Array

# TODO: do not use first element
# TODO: use swap


class PriorityQueue(object):
    def __init__(self):
        self.values = Array()
        self.values.append(None)

    def push(self, value):
        self.values.append(value)
        self.swim(len(self.values) - 1)

    def pop_min(self):
        if len(self.values) == 1:
            raise IndexError("pop from empty {}".format(self.__class__.__name__))

        self.swap(1, -1)
        value = self.values.pop()
        self.sink(1)

        return value

    def __len__(self):
        return len(self.values) - 1

    # TODO: break?
    def swim(self, i):
        while i >= 2:
            j = i // 2
            if self.values[j] > self.values[i]:
                self.swap(i, j)

            i = j

    def sink(self, i):
        while i * 2 < len(self.values):
            j = i * 2

            if j + 1 < len(self.values) and self.values[j] > self.values[j + 1]:
                j += 1

            if self.values[i] > self.values[j]:
                self.swap(i, j)
            else:
                break

            i = j

    def swap(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]
