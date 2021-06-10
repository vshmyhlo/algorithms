class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, value):
        self.head = Node(value=value, next=self.head)
        self.size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty {}".format(self.__class__.__name__))

        node = self.head
        self.head = node.next
        self.size -= 1

        return node.value

    def __delitem__(self, target):
        if not 0 <= target < self.size:
            raise IndexError("{} index out of range".format(self.__class__.__name__))

        self.head = delitem(self.head, target, 0)

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.value

            node = node.next


def delitem(node, target, i):
    if node is None:
        return None

    if target == i:
        return node.next

    node.next = delitem(node.next, target, i + 1)

    return node
