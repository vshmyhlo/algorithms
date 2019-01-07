from containers.queue import LinkedListQueue, ArrayQueue
import pytest


@pytest.fixture(params=[LinkedListQueue, ArrayQueue])
def xs(request):
    return request.param()


def test_enqueue_dequeue(xs):
    assert len(xs) == 0

    with pytest.raises(IndexError):
        xs.dequeue()

    xs.enqueue(1)
    xs.enqueue(2)
    xs.enqueue(3)

    assert len(xs) == 3
    assert xs.dequeue() == 1
    assert len(xs) == 2


def test_iter(xs):
    assert list(xs) == []

    xs.enqueue(1)
    xs.enqueue(2)
    xs.dequeue()
    xs.enqueue(3)

    assert list(xs) == [2, 3]
