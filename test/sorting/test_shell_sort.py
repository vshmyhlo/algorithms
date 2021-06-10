import numpy as np

from sorting.shell_sort import shell_sort


def test_sort():
    xs = list(np.random.randint(0, 1000, size=[1000]))
    assert shell_sort(xs) is None
    assert xs == sorted(xs)
