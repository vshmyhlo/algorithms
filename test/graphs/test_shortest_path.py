import pytest

from graphs.shortest_path_1 import ShortestPath as ShortestPath1
from graphs.shortest_path_2 import ShortestPath as ShortestPath2
from graphs.weighted_directed_graph import (WeightedDirectedEdge,
                                            WeightedDirectedGraph)


@pytest.fixture
def graph():
    g = WeightedDirectedGraph(9)
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
    return g


# TODO: more cases
@pytest.mark.parametrize("build_sp", [ShortestPath1, ShortestPath2])
def test_has_path_to(graph, build_sp):
    sp = build_sp(graph, 0)
    for v in range(8):
        assert sp.has_path_to(v)

    assert not sp.has_path_to(8)


# TODO: more cases
@pytest.mark.parametrize("build_sp", [ShortestPath1, ShortestPath2])
def test_path_to(graph, build_sp):
    sp = build_sp(graph, 0)
    assert list(sp.path_to(3)) == [
        WeightedDirectedEdge(0, 4, 9),
        WeightedDirectedEdge(4, 5, 4),
        WeightedDirectedEdge(5, 2, 1),
        WeightedDirectedEdge(2, 3, 3),
    ]

    assert sp.path_to(8) is None


# TODO: more cases
@pytest.mark.parametrize("build_sp", [ShortestPath1, ShortestPath2])
def test_distance_to(graph, build_sp):
    sp = build_sp(graph, 0)
    assert sp.distance_to(3) == 17
    assert sp.distance_to(8) == float("inf")
