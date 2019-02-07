import pytest
from graphs.graph import Graph
from graphs.connected_components import ConnectedComponents


@pytest.fixture
def cc():
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

    cc = ConnectedComponents(g)

    return cc


def test_connected(cc):
    assert cc.connected(0, 3)
    assert cc.connected(7, 8)
    assert cc.connected(9, 12)

    assert not cc.connected(0, 7)
    assert not cc.connected(0, 9)
    assert not cc.connected(7, 9)


def test_component_id(cc):
    assert cc.component_id(0) == 0
    assert cc.component_id(7) == 1
    assert cc.component_id(9) == 2


def test_len(cc):
    assert len(cc) == 3
