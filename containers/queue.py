class LinkedListQueue(object):
    class Node(object):
        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def enqueue(self, value):
        back = self.Node(value=value, next=None)

        if self.back is None:
            self.front = self.back = back
        else:
            self.back.next = back
            self.back = back

        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('dequeue from empty {}'.format(self.__class__.__name__))

        front = self.front
        self.front = front.next

        if self.front is None:
            self.back = None

        self.size -= 1

        return front.value

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.front

        while node is not None:
            yield node.value

            node = node.next


# TODO:
class ArrayQueue(object):
    pass
