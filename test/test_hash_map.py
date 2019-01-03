import pytest
from hash_map import HashMap


def test_getitem_setitem():
    x = HashMap()

    with pytest.raises(KeyError):
        x['key']

    x['key'] = 1
    assert x['key'] == 1
    x['key'] = 2
    assert x['key'] == 2


def test_delitem():
    x = HashMap()

    with pytest.raises(KeyError):
        del x['key']

    x['key'] = 1
    assert x['key'] == 1
    del x['key']

    with pytest.raises(KeyError):
        x['key']


def test_len():
    x = HashMap()

    assert len(x) == 0
    x['key_1'] = 1
    x['key_2'] = 2
    assert len(x) == 2
    del x['key_1']
    assert len(x) == 1


def test_contains():
    x = HashMap()

    assert 'key' not in x
    x['key'] = 1
    assert 'key' in x
    del x['key']
    assert 'key' not in x
