from collections import namedtuple


class LinkedList(object):
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
