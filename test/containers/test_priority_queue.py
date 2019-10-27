import pytest
import numpy as np
from containers.priority_queue import PriorityQueue

size = 1000


@pytest.fixture
def pq():
    return PriorityQueue()


# TODO: interleaving push/pop
# TODO: better test case
def test_enqueue_dequeue(pq):
    assert len(pq) == 0

    with pytest.raises(IndexError):
        pq.pop_min()

    values = np.random.standard_normal(size)
    for v in values:
        pq.push(v)

    assert len(pq) == size

    values_sorted = [pq.pop_min() for _ in range(size)]

    assert len(pq) == 0
    assert values_sorted == sorted(values)
