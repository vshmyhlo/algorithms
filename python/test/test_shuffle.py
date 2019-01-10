import numpy as np
from shuffle import shuffle


def test_shuffle():
    xs = list(np.arange(1000))
    copy = xs.copy()
    assert shuffle(xs) != xs
    assert sorted(shuffle(xs)) == xs
    assert xs == copy
