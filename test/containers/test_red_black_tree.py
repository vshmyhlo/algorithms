import numpy as np

from containers.red_black_tree import RedBlackTree


def test_red_black_tree():
    rng = np.random.RandomState(42)
    tree = RedBlackTree()

    keys = rng.randint(100, size=(1000,))
    for k in keys:
        tree[k] = str(k)

    assert len(tree) == len(np.unique(keys))
    assert np.array_equal(list(tree), sorted(np.unique(keys)))


def test_node_rotate_left():
    pass

    # l = Node('k1', 'v1')
    # r = Node('k1', 'v2')
    # node = Node('k', 'v', left=l, right=r, is_red=True)
