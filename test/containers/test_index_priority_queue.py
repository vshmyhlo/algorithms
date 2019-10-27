import pytest
import numpy as np
from shuffle import shuffle
from containers.index_priority_queue import IndexPriorityQueue

size = 1000


@pytest.fixture
def pq():
    return IndexPriorityQueue(size)


# TODO: interleaving push/pop
# TODO: better test case
def test_enqueue_dequeue(pq):
    assert len(pq) == 0

    with pytest.raises(IndexError):
        pq.pop_min()

    values = list(zip(np.random.permutation(size), np.random.standard_normal(size)))
    for k, v in values:
        pq.push(k, v)

    shuffle(values)
    for k, v in values:
        pq.decrease(k, v - 1.)

    assert len(pq) == size

    values_sorted = [pq.pop_min() for _ in range(size)]

    assert len(pq) == 0
    assert values_sorted == [i for i, _ in sorted(values, key=lambda x: x[1])]


def test_contains(pq):
    pq.push(200, 2.0)
    pq.push(100, 1.0)
    pq.push(300, 3.0)

    assert 200 in pq
    pq.pop_min()
    assert 200 in pq
    pq.pop_min()
    assert 200 not in pq
