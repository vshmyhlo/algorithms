from containers.array import Array
from containers.linked_list import LinkedList


class LinkedListStack(LinkedList):
    pass


class ArrayStack(Array):
    def push(self, value):
        self.append(value)
