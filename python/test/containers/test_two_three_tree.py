import numpy as np
import pytest

from containers.two_three_tree import TwoThreeTree


@pytest.mark.skip
def test_two_three_tree():
    rng = np.random.RandomState(42)
    x = TwoThreeTree()

    keys = rng.randint(100, size=(1000,))
    for k in keys:
        x[k] = str(k)

    print(list(x))
    print([x[k] for k in x])
