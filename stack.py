# TODO: test


class Stack(object):
    def __init__(self):
        self.size = 0
        self.node = None

    def push(self, item):
        self.node = item, self.node
        self.size += 1

    def pop(self):
        if self.node is None:
            raise IndexError('pop from empty stack')

        value, next = self.node
        self.node = next
        self.size -= 1
        return value

    def __len__(self):
        return self.size
