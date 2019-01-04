from collections import namedtuple

Node = namedtuple('Node', ['prev', 'value', 'next'])


class DoublyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def append_front(self, item):
        prev = None, item, self.front
        next = prev, self.front.value,
        self.front = item

        self.front = new
        self.size += 1

    def append_back(self, item):
        self.back = item, self.front
        self.size += 1

    def pop_front(self):
        if self.front is None:
            raise IndexError('pop from empty list')

        value, next = self.front
        self.front = next
        self.size -= 1
        return value

    def pop_back(self):
        pass

    def __len__(self):
        return self.size
