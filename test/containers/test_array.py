import pytest

from containers.array import Array


def test_getitem_setitem():
    xs = Array()

    with pytest.raises(IndexError):
        xs[0]

    xs.append(1)
    assert xs[0] == 1
    xs.append(2)
    assert xs[1] == 2

    with pytest.raises(IndexError):
        xs[3]


def test_len():
    xs = Array()

    assert len(xs) == 0
    xs.append(1)
    xs.append(2)
    xs.append(3)
    assert len(xs) == 3


def test_append_pop():
    xs = Array()

    assert len(xs) == 0

    with pytest.raises(IndexError):
        xs.pop()

    xs.append(1)
    xs.append(2)
    xs.append(3)

    assert len(xs) == 3
    assert xs.pop() == 3
    assert len(xs) == 2


def test_iter():
    xs = Array()

    assert list(xs) == []

    xs.append(1)
    xs.append(2)
    xs.pop()
    xs.append(3)

    assert list(xs) == [3, 1]
