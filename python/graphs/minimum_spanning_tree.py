from union_find import UnionFind


def minimum_spanning_tree(graph):
    edges = sorted(graph.edges())

    union_find = UnionFind(graph.num_vertices)

    for e in edges:
        v = e.either()
        w = e.other(v)

        if not union_find.connected(v, w):
            union_find.union(v, w)
            yield e
