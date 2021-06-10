import numpy as np

from is_sym import is_sym


def test_is_sym():
    ps = np.array(
        [
            [-2, 1],
            [0, 1],
            [-2, 1],
            [0, 1],
            [-2, 1],
            [0, 1],
        ]
    )

    assert is_sym(ps)

    ps = np.array(
        [
            [-2, 1],
            [-2, 2],
            [-2, 1],
            [0, 1],
            [0, 1],
            [0, 2],
        ]
    )

    assert is_sym(ps)
