# TODO: test


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.node = None

    def append(self, item):
        self.node = item, self.node
        self.size += 1

    def pop(self):
        if self.node is None:
            raise IndexError('pop from empty list')

        value, next = self.node
        self.node = next
        self.size -= 1
        return value

    def __len__(self):
        return self.size
