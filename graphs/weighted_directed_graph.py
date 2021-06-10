class WeightedDirectedGraph(object):
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.num_edges = 0

    def add_edge(self, e):
        self.adj_list[e.fr].append(e)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj_list[v]

    def edges(self):
        for v in range(self.num_vertices):
            yield from self.adjacent(v)


class WeightedDirectedEdge(object):
    def __init__(self, fr, to, weight):
        self.fr = fr
        self.to = to
        self.weight = weight

    def __eq__(self, other):
        return self.weight.__eq__(other.weight)

    def __ne__(self, other):
        return self.weight.__ne__(other.weight)

    def __lt__(self, other):
        return self.weight.__lt__(other.weight)

    def __le__(self, other):
        return self.weight.__le__(other.weight)

    def __gt__(self, other):
        return self.weight.__gt__(other.weight)

    def __ge__(self, other):
        return self.weight.__ge__(other.weight)

    def __repr__(self):
        return "{}({}, {}, {})".format(
            WeightedDirectedEdge.__name__, self.fr, self.to, self.weight
        )
