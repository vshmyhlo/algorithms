class WeightedGraph(object):
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.num_edges = 0

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj_list[v].append(e)
        self.adj_list[w].append(e)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj_list[v]


class WeightedEdge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError('vertex {} is not in the edge'.format(vertex))

    def __abs__(self):
        return 1

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
