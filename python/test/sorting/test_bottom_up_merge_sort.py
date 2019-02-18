import numpy as np
from sorting.bottom_up_merge_sort import bottom_up_merge_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert bottom_up_merge_sort(xs) is None
    assert xs == sorted(xs)
