import numpy as np
from sorting.selection_sort import selection_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert selection_sort(xs) is None
    assert xs == sorted(xs)
