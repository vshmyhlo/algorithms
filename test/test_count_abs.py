import numpy as np

from count_abs import count_abs


def test_count_abs():
    seq = []
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [1]
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [1, 1]
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [-1, 1]
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [-2] * 5
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [2] * 5
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = [-9, -8, -6, -6, -3, -2, 5, 5, 8, 8]
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = sorted(np.random.randint(-5, 5, size=5))
    assert count_abs(seq) == len(set(np.abs(seq)))

    seq = sorted(np.random.randint(-5, 5, size=10))
    assert count_abs(seq) == len(set(np.abs(seq)))
