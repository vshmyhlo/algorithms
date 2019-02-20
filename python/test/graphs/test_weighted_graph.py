import pytest
from graphs.weighted_graph import WeightedGraph, WeightedEdge


@pytest.fixture
def graph():
    g = WeightedGraph(4)

    g.add_edge(WeightedEdge(0, 1, 0.1))
    g.add_edge(WeightedEdge(0, 2, 0.2))
    g.add_edge(WeightedEdge(0, 3, 0.3))
    g.add_edge(WeightedEdge(1, 2, 1.2))

    return g


def test_weighted_graph(graph):
    edges = list(graph.edges())

    assert edges == [
        WeightedEdge(0, 1, 0.1),
        WeightedEdge(0, 2, 0.2),
        WeightedEdge(0, 3, 0.3),
        WeightedEdge(1, 2, 1.2)
    ]
