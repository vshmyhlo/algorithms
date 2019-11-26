import pytest

from containers.stack import LinkedListStack, ArrayStack


@pytest.fixture(params=[LinkedListStack, ArrayStack])
def seq(request):
    return request.param()


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
