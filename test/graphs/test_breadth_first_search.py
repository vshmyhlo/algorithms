import pytest

from graphs.breadth_first_search import BreadthFirstSearch
from graphs.graph import Graph


@pytest.fixture
def bfs():
    g = Graph(7)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(0, 5)

    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(2, 4)

    bfs = BreadthFirstSearch(g, 0)

    return bfs


def test_has_path_to(bfs):
    assert bfs.has_path_to(3)
    assert bfs.has_path_to(0)
    assert not bfs.has_path_to(6)


def test_path_to(bfs):
    assert list(bfs.path_to(3)) == [0, 2, 3]
    assert list(bfs.path_to(0)) == [0]
    assert bfs.path_to(6) is None


def test_distance_to(bfs):
    assert bfs.distance_to(3) == 2
    assert bfs.distance_to(0) == 0
    assert bfs.distance_to(6) is None
