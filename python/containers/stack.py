from collections import namedtuple


class LinkedListStack(object):
    Node = namedtuple('Node', ['value', 'next'])

    def __init__(self):
        self.size = 0
        self.node = None

    def push(self, value):
        self.node = self.Node(value=value, next=self.node)
        self.size += 1

    def pop(self):
        if self.node is None:
            raise IndexError('pop from empty {}'.format(self.__class__.__name__))

        node = self.node
        self.node = node.next
        self.size -= 1

        return node.value

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.node

        while node is not None:
            yield node.value

            node = node.next


class ArrayStack(object):
    def __init__(self):
        self.values = [None]
        self.size = 0

    def push(self, value):
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

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(self.size - 1, -1, -1):
            yield self.values[i]
