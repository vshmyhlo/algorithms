from union_find import UnionFind

# TODO: stop if v-1 edges in MST


def kruskal_mst(graph):
    union_find = UnionFind(graph.num_vertices)
    edges = sorted(graph.edges())

    for e in edges:
        v = e.either()
        w = e.other(v)

        if union_find.connected(v, w):
            continue

        union_find.union(v, w)
        yield e


def prim_mst(graph):
    fail
