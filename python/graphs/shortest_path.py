from containers.stack import LinkedListStack as Stack


class ShortedPath(object):
    def __init__(self, graph, source):
        self.source = source
        self.edge_to = [None] * graph.num_vertices
        self.dist_to = [float('inf')] * graph.num_vertices
        self.dist_to[source] = 0

        pass

    # TODO:
    def has_path_to(self, v):
        return self.dist_to[v] < float('inf')

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = Stack()
        e = self.edge_to[v]
        while e is not None:
            path.push(e)
            e = self.edge_to[e.fr]

        return path

    def distance_to(self, v):
        return self.dist_to[v]

    def relax(self, e):
        new_dist = self.dist_to[e.fr] + e.weight

        if new_dist < self.dist_to[e.to]:
            self.dist_to[e.to] = new_dist
            self.edge_to[e.to] = e
