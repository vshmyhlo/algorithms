from collections import namedtuple

Node = namedtuple('Node', ['value', 'next'])


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.node = None

    def append(self, value):
        self.node = Node(value=value, next=self.node)
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
