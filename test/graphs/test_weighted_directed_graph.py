import pytest
from graphs.weighted_directed_graph import WeightedDirectedGraph, WeightedDirectedEdge


@pytest.fixture
def graph():
    g = WeightedDirectedGraph(4)

    g.add_edge(WeightedDirectedEdge(0, 1, 0.1))
    g.add_edge(WeightedDirectedEdge(0, 2, 0.2))
    g.add_edge(WeightedDirectedEdge(0, 3, 0.3))
    g.add_edge(WeightedDirectedEdge(1, 2, 1.2))
    g.add_edge(WeightedDirectedEdge(3, 0, 3.0))

    return g


def test_graph_adjacent(graph):
    edges = list(graph.adjacent(0))

    assert edges == [
        WeightedDirectedEdge(0, 1, 0.1),
        WeightedDirectedEdge(0, 2, 0.2),
        WeightedDirectedEdge(0, 3, 0.3)
    ]


def test_graph_edges(graph):
    edges = list(graph.edges())

    assert edges == [
        WeightedDirectedEdge(0, 1, 0.1),
        WeightedDirectedEdge(0, 2, 0.2),
        WeightedDirectedEdge(0, 3, 0.3),
        WeightedDirectedEdge(1, 2, 1.2),
        WeightedDirectedEdge(3, 0, 3.0)
    ]
