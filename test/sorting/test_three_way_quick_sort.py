import numpy as np

from sorting.three_way_quick_sort import three_way_quick_sort


def test_sort():
    seq = list(np.random.randint(0, 1000, size=[1000]))
    assert three_way_quick_sort(seq) is None
    assert seq == sorted(seq)
