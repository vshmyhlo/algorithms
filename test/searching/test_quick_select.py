import numpy as np

from searching.quick_select import quick_select


def test_selection():
    seq = list(np.random.randint(0, 1000, size=[1000]))
    assert sorted(seq)[10] == quick_select(seq, 10)
