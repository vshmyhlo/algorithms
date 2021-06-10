import numpy as np
import pytest

from containers.binary_search_tree import BinarySearchTree

# TODO: refactor random state rng
# TODO: implement all methods (select, etc.)


def test_binary_search_tree():
    rng = np.random.RandomState(42)
    x = BinarySearchTree()
    assert len(x) == 0
    assert list(x) == []

    for i in rng.permutation(100):
        x[i] = str(i)

    assert len(x) == 100
    assert list(x) == list(range(100))

    for i in rng.permutation(100):
        assert x[i] == str(i)

    assert 42 in x
    del x[42]
    assert 42 not in x
    assert len(x) == 99

    with pytest.raises(KeyError):
        x[42]

    with pytest.raises(KeyError):
        del x[42]

    assert x.min() == 0
    assert x.max() == 99

    assert x.floor(42) == 41
    assert x.ceil(42) == 43

    with pytest.raises(ValueError):
        x.floor(-1)

    with pytest.raises(ValueError):
        x.ceil(100)

    assert x.rank(42) == 42

    x.delete_min()
    x.delete_max()

    assert 0 not in x
    assert 99 not in x

    assert x.min() == 1
    assert x.max() == 98
    assert len(x) == 97


def test_range_operations():
    rng = np.random.RandomState(42)
    tree = BinarySearchTree()

    for k in rng.permutation(100):
        tree[k] = str(k)

    lo, hi = 10, 15
    count = tree.range_count(lo, hi)
    search = list(tree.range_search(lo, hi))
    assert count == len(search)
    assert search == list(range(10, 15 + 1))

    lo, hi = 9.5, 15.5
    count = tree.range_count(lo, hi)
    search = list(tree.range_search(lo, hi))
    assert count == len(search)
    assert search == list(range(10, 15 + 1))

    lo, hi = 10, 10
    count = tree.range_count(lo, hi)
    search = list(tree.range_search(lo, hi))
    assert count == 1
    assert search == [10]

    lo, hi = 3.3, 3.7
    count = tree.range_count(lo, hi)
    search = list(tree.range_search(lo, hi))
    assert count == 0
    assert search == []
