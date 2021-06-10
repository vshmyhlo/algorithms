import pytest

from graphs.graph import Graph


@pytest.fixture
def graph():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(4, 4)

    return g


def test_add_edge(graph):
    assert 4 not in graph.adjacent(0)
    graph.add_edge(0, 4)
    assert 4 in graph.adjacent(0)


def test_adjacent(graph):
    assert list(graph.adjacent(0)) == [1, 2, 3]


def test_num_vertices(graph):
    assert graph.num_vertices == 5


def test_num_edges(graph):
    assert graph.num_edges == 5


def test_degree(graph):
    assert graph.degree(0) == 3


def test_max_degree(graph):
    assert graph.max_degree() == 3


def test_avg_degree(graph):
    assert graph.avg_degree() == 2


def test_num_self_loops(graph):
    assert graph.num_self_loops() == 1
