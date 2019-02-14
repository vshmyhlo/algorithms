from graphs.directed_graph import DirectedGraph
from graphs.topological_sort import topological_sort


def test_topological_sort():
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

    assert list(topological_sort(g)) == [3, 6, 0, 5, 2, 1, 4]
