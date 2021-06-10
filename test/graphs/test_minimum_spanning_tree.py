import pytest

from graphs.minimum_spanning_tree import kruskal_mst, prim_mst
from graphs.weighted_graph import WeightedEdge, WeightedGraph

# TODO: use parameterized fixture for different implementations


@pytest.fixture
def graph():
    g = WeightedGraph(8)

    g.add_edge(WeightedEdge(4, 5, 0.35))
    g.add_edge(WeightedEdge(4, 7, 0.37))
    g.add_edge(WeightedEdge(5, 7, 0.28))
    g.add_edge(WeightedEdge(0, 7, 0.16))
    g.add_edge(WeightedEdge(1, 5, 0.32))
    g.add_edge(WeightedEdge(0, 4, 0.38))
    g.add_edge(WeightedEdge(2, 3, 0.17))
    g.add_edge(WeightedEdge(1, 7, 0.19))
    g.add_edge(WeightedEdge(0, 2, 0.26))
    g.add_edge(WeightedEdge(1, 2, 0.36))
    g.add_edge(WeightedEdge(1, 3, 0.29))
    g.add_edge(WeightedEdge(2, 7, 0.34))
    g.add_edge(WeightedEdge(6, 2, 0.40))
    g.add_edge(WeightedEdge(3, 6, 0.52))
    g.add_edge(WeightedEdge(6, 0, 0.58))
    g.add_edge(WeightedEdge(6, 4, 0.93))

    return g


def test_kruskal_mst(graph):
    edges = list(kruskal_mst(graph))
    weight = sum(e.weight for e in edges)

    assert edges == [
        WeightedEdge(0, 7, 0.16),
        WeightedEdge(2, 3, 0.17),
        WeightedEdge(1, 7, 0.19),
        WeightedEdge(0, 2, 0.26),
        WeightedEdge(5, 7, 0.28),
        WeightedEdge(4, 5, 0.35),
        WeightedEdge(6, 2, 0.4),
    ]

    assert weight == 1.81


def test_prim_mst(graph):
    edges = list(prim_mst(graph))
    weight = sum(e.weight for e in edges)

    assert edges == [
        WeightedEdge(0, 7, 0.16),
        WeightedEdge(2, 3, 0.17),
        WeightedEdge(1, 7, 0.19),
        WeightedEdge(0, 2, 0.26),
        WeightedEdge(5, 7, 0.28),
        WeightedEdge(4, 5, 0.35),
        WeightedEdge(6, 2, 0.4),
    ]

    assert weight == 1.81
