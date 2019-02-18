import pytest
from graphs.directed_graph import DirectedGraph
from graphs.strong_connected_components import StrongConnectedComponents


@pytest.fixture
def cc():
    g = DirectedGraph(13)
    g.add_edge(0, 6)
    g.add_edge(6, 8)
    g.add_edge(8, 6)
    g.add_edge(6, 7)
    g.add_edge(0, 2)
    g.add_edge(2, 4)
    g.add_edge(4, 11)
    g.add_edge(11, 9)
    g.add_edge(9, 12)
    g.add_edge(12, 11)
    g.add_edge(12, 10)
    g.add_edge(10, 9)
    g.add_edge(9, 7)
    g.add_edge(9, 6)
    g.add_edge(4, 6)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 2)
    g.add_edge(5, 0)
    g.add_edge(2, 3)
    g.add_edge(1, 0)

    cc = StrongConnectedComponents(g.reverse())

    return cc


def test_connected(cc):
    assert cc.connected(0, 2)
    assert cc.connected(9, 12)
    assert cc.connected(6, 8)

    assert not cc.connected(0, 1)
    assert not cc.connected(5, 6)
    assert not cc.connected(8, 9)


def test_component_id(cc):
    ids = [1, 0, 1, 1, 1, 1, 3, 4, 3, 2, 2, 2, 2]

    for v, id in enumerate(ids):
        assert cc.component_id(v) == id


def test_len(cc):
    assert len(cc) == 5
