from containers.interval_search_tree import IntervalSearchTree


def test_interval_search_tree():
    tree = IntervalSearchTree()

    intervals = [
        (17, 19),
        (5, 8),
        (21, 24),
        (4, 8),
        (15, 18),
        (7, 10),
    ]

    for lo, hi in intervals:
        tree[lo, hi] = 'interval({}, {})'.format(lo, hi)

    assert tree.root.max == 24
    assert tree.root.left.max == 18
    assert tree.root.right.max == 24

    tree[16, 22] = 'interval(16, 22)'

    assert tree.root.max == 24
    assert tree.root.left.max == 22
    assert tree.root.right.max == 24

    assert tree.intersection_search((23, 25)) == (21, 24)
    assert tree.intersection_search((12, 14)) is None
    assert tree.intersection_search((21, 23)) == (16, 22)
