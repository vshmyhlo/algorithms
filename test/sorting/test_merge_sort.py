import numpy as np
from sorting.merge_sort import sort


def test_sorting():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert sort(xs) == sorted(xs)
