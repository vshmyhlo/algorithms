import pytest

from containers.queue import LinkedListQueue


# TODO: ArrayQueue
# @pytest.fixture(params=[LinkedListQueue, ArrayQueue])
@pytest.fixture(params=[LinkedListQueue])
def seq(request):
    return request.param()


def test_enqueue_dequeue(seq):
    assert len(seq) == 0

    with pytest.raises(IndexError):
        seq.dequeue()

    seq.enqueue(1)
    seq.enqueue(2)
    seq.enqueue(3)

    assert len(seq) == 3
    assert seq.dequeue() == 1
    assert len(seq) == 2


def test_iter(seq):
    assert list(seq) == []

    seq.enqueue(1)
    seq.enqueue(2)
    seq.dequeue()
    seq.enqueue(3)

    assert list(seq) == [2, 3]
