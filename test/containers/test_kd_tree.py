import numpy as np

from containers.kd_tree import KDTree


def test_kd_tree():
    tree = KDTree(2)
    ps = np.random.uniform(size=(100, 2)).tolist()

    for i in range(len(ps)):
        assert ps[i] not in tree
        tree[ps[i]] = str(i)
        assert ps[i] in tree

        for j in range(i + 1, len(ps)):
            assert ps[j] not in tree

    for i in range(len(ps)):
        assert ps[i] in tree
        assert tree[ps[i]] == str(i)

    p1 = [-0.25, -0.75]
    p2 = [0.75, 0.25]
    expected = [p for p in ps if p1[0] <= p[0] <= p2[0] and p1[1] <= p[1] <= p2[1]]
    assert sorted(tree.range_search(p1, p2)) == sorted(expected)
    # assert sorted(tree.range_count(p1, p2)) == len(expected)

    p1 = ps[0]
    p2 = ps[-1]
    expected = [p for p in ps if p1[0] <= p[0] <= p2[0] and p1[1] <= p[1] <= p2[1]]
    assert sorted(tree.range_search(p1, p2)) == sorted(expected)
    # assert sorted(tree.range_count(p1, p2)) == len(expected)
