import numpy as np

from sorting.insertion_sort import insertion_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert insertion_sort(xs) is None
    assert xs == sorted(xs)
