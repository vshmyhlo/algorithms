from containers.stack import LinkedListStack as Stack
from containers.index_priority_queue import IndexPriorityQueue


class ShortedPath(object):
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        self.edge_to = [None] * graph.num_vertices
        self.dist_to = [float('inf')] * graph.num_vertices
        self.dist_to[source] = 0

        priority = IndexPriorityQueue(graph.num_vertices)
        priority.push(source, self.dist_to[source])
        self.visited[source] = True

        while len(priority) > 0:
            v = priority.pop_min()

            for e in graph.adjacent(v):
                self.relax(e, priority)

    # TODO: use visited?
    def has_path_to(self, v):
        return self.visited[v]

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

    def relax(self, e, priority):
        new_dist = self.dist_to[e.fr] + e.weight

        if new_dist < self.dist_to[e.to]:
            self.dist_to[e.to] = new_dist
            self.edge_to[e.to] = e

            if e.to in priority:
                priority.decrease(e.to, self.dist_to[e.to])
            else:
                priority.push(e.to, self.dist_to[e.to])
                self.visited[e.to] = True
