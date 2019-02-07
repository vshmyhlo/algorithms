# TODO: check self-loops


class DepthFirstSearch(object):
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        self.edge_to = [None] * graph.num_vertices

        self.depth_first_search(graph, source)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        path = []

        if not self.has_path_to(v):
            return None

        while v != self.source:
            path.append(v)
            v = self.edge_to[v]

        path.append(self.source)

        return reversed(path)

    def depth_first_search(self, graph, v):
        self.visited[v] = True

        for w in graph.adjacent(v):
            if self.visited[w]:
                continue

            # TODO: is order important? think about parallel edges
            self.edge_to[w] = v
            self.depth_first_search(graph, w)
