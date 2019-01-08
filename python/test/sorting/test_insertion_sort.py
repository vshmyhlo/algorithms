import numpy as np
from sorting.insertion_sort import insertion_sort


def test_sorting():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    copy = xs.copy()
    assert insertion_sort(xs) == sorted(xs)
    assert xs == copy
