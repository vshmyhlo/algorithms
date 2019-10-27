import pytest
from graphs.graph import Graph
from graphs.depth_first_search import DepthFirstSearch


@pytest.fixture
def dfs():
    g = Graph(13)
    g.add_edge(0, 6)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(6, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 3)
    g.add_edge(5, 3)

    g.add_edge(7, 8)

    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(9, 12)
    g.add_edge(11, 12)

    dfs = DepthFirstSearch(g, 0)

    return dfs


def test_has_path_to(dfs):
    assert dfs.has_path_to(3)
    assert dfs.has_path_to(0)
    assert not dfs.has_path_to(7)


def test_path_to(dfs):
    assert list(dfs.path_to(3)) == [0, 6, 4, 5, 3]
    assert list(dfs.path_to(0)) == [0]
    assert dfs.path_to(7) is None
