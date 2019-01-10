import pytest
import numpy as np
from containers.priority_queue import PriorityQueue


# TODO: interleaving push/pop
# TODO: better test case
def test_enqueue_dequeue():
    xs = PriorityQueue()

    assert len(xs) == 0

    with pytest.raises(IndexError):
        xs.pop_max()

    for x in np.random.randint(0, 1000, size=[1000]):
        xs.push(x)

    assert len(xs) == 1000

    tmp = []
    for _ in range(1000):
        tmp.append(xs.pop_max())

    assert len(xs) == 0

    assert tmp == sorted(tmp, reverse=True)
