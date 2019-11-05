import numpy as np

from sorting.quick_sort import quick_sort


def test_sort():
    seq = list(np.random.randint(0, 1000, size=[1000]))
    assert quick_sort(seq) is None
    assert seq == sorted(seq)
