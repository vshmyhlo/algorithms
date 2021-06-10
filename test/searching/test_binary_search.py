import numpy as np

from searching.binary_search import binary_search


def test_search():
    xs = sorted(np.random.normal(size=[1000]))
    x = xs[np.random.randint(1000)]
    assert binary_search(xs, x) == xs.index(x)


def test_not_found():
    xs = sorted(np.random.normal(size=[1000]))
    assert binary_search(xs, 0) is None
