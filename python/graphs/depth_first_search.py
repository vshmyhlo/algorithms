# TODO: check self-loops
from containers.stack import LinkedListStack as Stack


class DepthFirstSearch(object):
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        self.edge_to = [None] * graph.num_vertices

        self.depth_first_search(graph, source)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = Stack()
        while v != self.source:
            path.push(v)
            v = self.edge_to[v]

        path.push(self.source)

        return path

    def depth_first_search(self, graph, v):
        self.visited[v] = True

        for w in graph.adjacent(v):
            if self.visited[w]:
                continue

            # TODO: is order important? think about parallel edges
            self.edge_to[w] = v
            self.depth_first_search(graph, w)
