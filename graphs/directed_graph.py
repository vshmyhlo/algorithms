class DirectedGraph(object):
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.num_edges = 0

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj_list[v]

    def reverse(self):
        graph = DirectedGraph(self.num_vertices)

        for v in range(self.num_vertices):
            for w in self.adjacent(v):
                graph.add_edge(w, v)

        return graph
