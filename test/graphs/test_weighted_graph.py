import pytest

from graphs.weighted_graph import WeightedEdge, WeightedGraph


@pytest.fixture
def graph():
    g = WeightedGraph(4)

    g.add_edge(WeightedEdge(0, 1, 0.1))
    g.add_edge(WeightedEdge(0, 2, 0.2))
    g.add_edge(WeightedEdge(0, 3, 0.3))
    g.add_edge(WeightedEdge(1, 2, 1.2))

    return g


@pytest.fixture
def edge():
    return WeightedEdge(1, 2, 1.2)


def test_graph_adjacent(graph):
    edges = list(graph.adjacent(0))

    assert edges == [
        WeightedEdge(0, 1, 0.1),
        WeightedEdge(0, 2, 0.2),
        WeightedEdge(0, 3, 0.3),
    ]


def test_graph_edges(graph):
    edges = list(graph.edges())

    assert edges == [
        WeightedEdge(0, 1, 0.1),
        WeightedEdge(0, 2, 0.2),
        WeightedEdge(0, 3, 0.3),
        WeightedEdge(1, 2, 1.2),
    ]


def test_edge_either(edge):
    assert edge.either() == 1


def test_edge_other(edge):
    assert edge.other(1) == 2
    assert edge.other(2) == 1

    with pytest.raises(ValueError):
        edge.other(0)
