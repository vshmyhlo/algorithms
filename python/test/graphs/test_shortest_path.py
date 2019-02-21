import pytest
from graphs.weighted_directed_graph import WeightedDirectedGraph, WeightedDirectedEdge
from graphs.shortest_path import ShortedPath


@pytest.fixture
def sp():
    g = WeightedDirectedGraph(8)
    g.add_edge(WeightedDirectedEdge(0, 1, 5))
    g.add_edge(WeightedDirectedEdge(0, 7, 8))
    g.add_edge(WeightedDirectedEdge(0, 4, 9))
    g.add_edge(WeightedDirectedEdge(1, 3, 15))
    g.add_edge(WeightedDirectedEdge(1, 2, 12))
    g.add_edge(WeightedDirectedEdge(1, 7, 4))
    g.add_edge(WeightedDirectedEdge(7, 5, 6))
    g.add_edge(WeightedDirectedEdge(7, 2, 7))
    g.add_edge(WeightedDirectedEdge(4, 7, 5))
    g.add_edge(WeightedDirectedEdge(4, 5, 4))
    g.add_edge(WeightedDirectedEdge(4, 6, 20))
    g.add_edge(WeightedDirectedEdge(5, 2, 1))
    g.add_edge(WeightedDirectedEdge(5, 6, 13))
    g.add_edge(WeightedDirectedEdge(2, 3, 3))
    g.add_edge(WeightedDirectedEdge(2, 6, 11))
    g.add_edge(WeightedDirectedEdge(3, 6, 9))

    shortest_path = ShortedPath(g, 0)

    return shortest_path


def test_has_path_to(sp):
    for v in range(8):
        assert sp.has_path_to(v)


# TODO: more cases
def test_path_to(sp):
    assert sp.path_to(3) == [
        WeightedDirectedEdge(0, 4, 9),
        WeightedDirectedEdge(4, 5, 4),
        WeightedDirectedEdge(5, 2, 1),
        WeightedDirectedEdge(2, 3, 3)
    ]


# TODO: more cases
def test_distance_to(sp):
    assert sp.dist_to(3) == 17
