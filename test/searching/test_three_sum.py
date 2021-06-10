import itertools

import numpy as np

from searching.three_sum import three_sum


def test_sum():
    size = 100
    xs = list(np.random.randint(-size, size, size=[size]))
    actual = three_sum(xs)
    expected = 0

    for values in itertools.combinations(xs, 3):
        if sum(values) == 0:
            expected += 1

    assert actual == expected
