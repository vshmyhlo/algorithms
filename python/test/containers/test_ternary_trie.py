from containers.ternary_trie import TernaryTrie


def test_ternary_trie():
    tree = TernaryTrie()
    keys = [
        'by',
        'sea',
        'sells',
        'she',
        'shells',
        'shore',
        'the',
    ]

    for k in keys:
        assert k not in tree
        assert tree[k] is None

    for i in range(len(keys)):
        tree[keys[i]] = i
        assert keys[i] in tree
        assert tree[keys[i]] == i

        for j in range(i + 1, len(keys)):
            assert keys[j] not in tree

    assert list(tree) == sorted(keys)
    assert list(tree.keys_with_prefix('sh')) == sorted(['she', 'shells', 'shore'])
    assert list(tree.keys_with_prefix('she')) == sorted(['she', 'shells'])
    assert list(tree.keys_with_prefix('no')) == []

    assert tree.longest_prefix_of('sheep') == 'she'
    assert tree.longest_prefix_of('shore') == 'shore'
    assert tree.longest_prefix_of('shoes') == ''

    for i in range(len(keys)):
        del tree[keys[i]]
        assert keys[i] not in tree
        assert tree[keys[i]] is None

        for j in range(i + 1, len(keys)):
            assert keys[j] in tree
