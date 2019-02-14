class DirectedGraph(object):
    def __init__(self, n_v):
        self.adj_list = [[] for _ in range(n_v)]
        self.num_vertices = n_v
        self.num_edges = 0

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj_list[v]

    def reverse(self, v):
        pass
