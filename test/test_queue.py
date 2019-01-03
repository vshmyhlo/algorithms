from queue import Queue
import pytest


def test_append_pop():
    xs = Queue()

    assert len(xs) == 0

    with  pytest.raises(IndexError):
        xs.pop()

    xs.push(1)
    xs.push(2)
    assert len(xs) == 2
    assert xs.pop() == 1
    assert len(xs) == 1
