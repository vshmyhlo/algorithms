from containers.stack import LinkedListStack, ArrayStack
import pytest


@pytest.fixture(params=[LinkedListStack, ArrayStack])
def xs(request):
    return request.param()


def test_push_pop(xs):
    assert len(xs) == 0

    with pytest.raises(IndexError):
        xs.pop()

    xs.push(1)
    xs.push(2)
    xs.push(3)

    assert len(xs) == 3
    assert xs.pop() == 3
    assert len(xs) == 2


def test_iter(xs):
    assert list(xs) == []

    xs.push(1)
    xs.push(2)
    xs.pop()
    xs.push(3)

    assert list(xs) == [3, 1]
