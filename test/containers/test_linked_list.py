import pytest

from containers.linked_list import LinkedList


@pytest.fixture
def seq():
    return LinkedList()


def test_push_pop(seq):
    assert len(seq) == 0

    with pytest.raises(IndexError):
        seq.pop()

    seq.push(1)
    seq.push(2)
    seq.push(3)

    assert len(seq) == 3
    assert seq.pop() == 3
    assert len(seq) == 2


def test_iter(seq):
    assert list(seq) == []

    seq.push(1)
    seq.push(2)
    seq.pop()
    seq.push(3)

    assert list(seq) == [3, 1]


def test_delitem(seq):
    with pytest.raises(IndexError):
        del seq[0]

    for i in range(3):
        seq.push(i + 1)

    with pytest.raises(IndexError):
        del seq[3]

    del seq[1]

    assert list(seq) == [3, 1]
