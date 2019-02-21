# TODO: use array
# TODO: maybe use dict and do not use size
# TODO: do not use first element
class IndexPriorityQueue(object):
    def __init__(self, size):
        self.key_to_ind = [None] * (size + 1)
        self.ind_to_key = [None] * (size + 1)
        self.ind_to_val = [None] * (size + 1)
        self.size = 1

    def push(self, key, value):
        i = self.size
        self.key_to_ind[key] = i
        self.ind_to_key[i] = key
        self.ind_to_val[i] = value

        self.size += 1
        self.swim(i)

    def pop_min(self):
        if self.size == 1:
            raise IndexError('pop from empty {}'.format(self.__class__.__name__))

        j = self.size - 1
        self.swap(1, j)

        key = self.ind_to_key[j]
        self.key_to_ind[key] = None
        self.ind_to_key[j] = None
        self.ind_to_val[j] = None

        self.size -= 1
        self.sink(1)

        return key

    def decrease(self, key, value):
        i = self.key_to_ind[key]
        assert self.ind_to_key[i] == key  # TODO: checks invariant, remove
        self.ind_to_val[i] = value

        self.swim(i)

    def __len__(self):
        return self.size - 1

    def swim(self, i):
        while i >= 2:
            j = i // 2
            if self.ind_to_val[j] > self.ind_to_val[i]:
                self.swap(i, j)

            i = j

    def sink(self, i):
        while i * 2 < self.size:
            j = i * 2

            if j + 1 < self.size and self.ind_to_val[j] > self.ind_to_val[j + 1]:
                j += 1

            if self.ind_to_val[i] > self.ind_to_val[j]:
                self.swap(i, j)
            else:
                break

            i = j

    def swap(self, i, j):
        self.key_to_ind[self.ind_to_key[i]], self.key_to_ind[self.ind_to_key[j]] = j, i
        self.ind_to_key[i], self.ind_to_key[j] = self.ind_to_key[j], self.ind_to_key[i]
        self.ind_to_val[i], self.ind_to_val[j] = self.ind_to_val[j], self.ind_to_val[i]
