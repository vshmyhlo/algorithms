import pytest

from containers.hash_map import HashMap


@pytest.fixture
def hash_map():
    return HashMap(32)


def test_hash_map(hash_map):
    n = 100

    assert len(hash_map) == 0
    assert sorted(hash_map) == []

    for i in range(n):
        with pytest.raises(KeyError):
            del hash_map[i]

    for i in range(n):
        hash_map[i] = str(i)
        assert i in hash_map
        assert hash_map[i] == str(i)

        for j in range(i + 1, n):
            assert j not in hash_map

    assert len(hash_map) == n
    assert sorted(hash_map) == list(range(n))

    for i in range(n):
        del hash_map[i]
        assert i not in hash_map
        assert len(hash_map) == n - i - 1

        for j in range(i + 1, n):
            assert j in hash_map

    assert len(hash_map) == 0
    assert sorted(hash_map) == []
