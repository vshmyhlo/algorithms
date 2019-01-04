class Node(object):
    def __init__(self, prev, value, next):
        self.prev = prev
        self.value = value
        self.next = next


class DoublyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def append_front(self, value):
        front = Node(prev=None, value=value, next=None)
        link(front, self.front)
        self.front = front

        if self.back is None:
            self.back = front

        self.size += 1

    def append_back(self, value):
        back = Node(prev=None, value=value, next=None)
        link(self.back, back)
        self.back = back

        if self.front is None:
            self.front = back

        self.size += 1

    def pop_front(self):
        if self.front is None:
            raise IndexError('pop from empty list')

        front = self.front
        self.front = front.next
        unlink(front, self.front)

        self.size -= 1

        return front.value

    def pop_back(self):
        if self.back is None:
            raise IndexError('pop from empty list')

        back = self.back
        self.back = back.prev
        unlink(self.back, back)

        self.size -= 1

        return back.value

    def __len__(self):
        return self.size


def link(prev, next):
    if prev is not None:
        prev.next = next

    if next is not None:
        next.prev = prev


def unlink(prev, next):
    if prev is not None:
        prev.next = None

    if next is not None:
        next.prev = None
