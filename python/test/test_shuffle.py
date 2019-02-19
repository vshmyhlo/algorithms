import numpy as np
from shuffle import shuffle


def test_shuffle():
    xs = list(np.arange(1000))
    assert shuffle(xs) is None
    assert xs != sorted(xs)
