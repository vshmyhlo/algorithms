from containers.doubly_linked_list import DoublyLinkedList
import pytest


def test_append_pop():
    xs = DoublyLinkedList()

    assert len(xs) == 0

    with pytest.raises(IndexError):
        xs.pop_front()

    with pytest.raises(IndexError):
        xs.pop_back()

    xs.append_front(1)
    xs.append_back(2)
    xs.append_back(3)
    assert len(xs) == 3

    assert xs.pop_front() == 1
    assert xs.pop_front() == 2
    assert xs.pop_back() == 3
    assert len(xs) == 0
