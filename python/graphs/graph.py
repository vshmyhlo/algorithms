class Graph(object):
    def __init__(self, n_v):
        self.adj_list = [[] for _ in range(n_v)]
        self.num_vertices = n_v
        self.num_edges = 0

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj_list[v]

    def degree(self, v):
        return sum(1 for _ in self.adjacent(v))

    def max_degree(self):
        return max(self.degree(v) for v in range(self.num_vertices))

    def avg_degree(self):
        return 2 * self.num_edges / self.num_vertices

    def num_self_loops(self):
        count = 0
        for v in range(self.num_vertices):
            for w in self.adjacent(v):
                if v == w:
                    count += 1

        return count / 2
