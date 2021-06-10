import pytest

from graphs.directed_graph import DirectedGraph


@pytest.fixture
def graph():
    g = DirectedGraph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(3, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(5, 2)
    g.add_edge(6, 0)
    g.add_edge(6, 4)

    return g


def test_add_edge(graph):
    assert 4 not in graph.adjacent(0)
    assert 0 not in graph.adjacent(4)

    graph.add_edge(0, 4)

    assert 4 in graph.adjacent(0)
    assert 0 not in graph.adjacent(4)


def test_adjacent(graph):
    assert list(graph.adjacent(0)) == [1, 5, 2]


def test_num_vertices(graph):
    assert graph.num_vertices == 7


def test_num_edges(graph):
    assert graph.num_edges == 11


def test_reverse(graph):
    fail
