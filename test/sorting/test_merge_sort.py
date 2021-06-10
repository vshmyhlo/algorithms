import numpy as np

from sorting.merge_sort import merge_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    copy = xs.copy()
    assert merge_sort(xs) == sorted(xs)
    assert xs == copy
