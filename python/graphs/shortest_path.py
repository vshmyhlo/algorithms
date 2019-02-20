from containers.stack import LinkedListStack as Stack


class ShortedPath(object):
    def __init__(self, graph, source):
        self.source = source
        self.edge_to = [None] * graph.num_vertices
        self.dist_to = [None] * graph.num_vertices

    def has_path_to(self, v):
        pass

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
