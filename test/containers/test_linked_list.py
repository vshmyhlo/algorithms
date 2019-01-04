from containers.linked_list import LinkedList
import pytest


def test_append_pop():
    xs = LinkedList()

    assert len(xs) == 0

    with  pytest.raises(IndexError):
        xs.pop()

    xs.append(1)
    xs.append(2)
    assert len(xs) == 2
    assert xs.pop() == 2
    assert len(xs) == 1
