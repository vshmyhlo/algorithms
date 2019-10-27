import numpy as np
from sorting.heap_sort import heap_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert heap_sort(xs) is None
    assert xs == sorted(xs)
