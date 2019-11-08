import numpy as np

from sorting.parallel_merge_sort import parallel_merge_sort


def test_parallel_merge_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    copy = xs.copy()
    assert parallel_merge_sort(xs) == sorted(xs)
    assert xs == copy
