import numpy as np
from sorting.quick_sort import quick_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    copy = xs.copy()
    assert quick_sort(xs) == sorted(xs)
    assert xs == copy
