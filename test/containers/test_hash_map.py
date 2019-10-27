import pytest
from containers.hash_map import HashMap


@pytest.fixture
def hash_map():
    return HashMap()


def test_getitem_setitem(hash_map):
    with pytest.raises(KeyError):
        hash_map['key']

    hash_map['key'] = 1
    assert hash_map['key'] == 1
    hash_map['key'] = 2
    assert hash_map['key'] == 2


def test_delitem(hash_map):
    with pytest.raises(KeyError):
        del hash_map['key']

    hash_map['key'] = 1
    assert hash_map['key'] == 1
    del hash_map['key']

    with pytest.raises(KeyError):
        hash_map['key']


def test_len(hash_map):
    assert len(hash_map) == 0
    hash_map['key_1'] = 1
    hash_map['key_2'] = 2
    assert len(hash_map) == 2
    del hash_map['key_1']
    assert len(hash_map) == 1


def test_contains(hash_map):
    assert 'key' not in hash_map
    hash_map['key'] = 1
    assert 'key' in hash_map
    del hash_map['key']
    assert 'key' not in hash_map


def test_iter(hash_map):
    keys = list(range(1000))

    for k in keys:
        hash_map[k] = str(k)

    assert sorted(list(hash_map)) == keys
