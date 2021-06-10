from containers.priority_queue import PriorityQueue
from containers.stack import LinkedListStack as Stack


class ShortestPath(object):
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        self.parent = [None] * graph.num_vertices
        self.dist = [float("inf")] * graph.num_vertices
        self.dist[source] = 0

        queue = PriorityQueue()
        queue.push((self.dist[source], source))

        while len(queue) > 0:
            d, v = queue.pop_min()
            if self.visited[v]:
                continue
            self.visited[v] = True

            for e in graph.adjacent(v):
                new_dist = self.dist[e.fr] + e.weight

                if new_dist < self.dist[e.to]:
                    self.dist[e.to] = new_dist
                    self.parent[e.to] = e

                    queue.push((self.dist[e.to], e.to))

    # TODO: use visited?
    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = Stack()
        e = self.parent[v]
        while e is not None:
            path.push(e)
            e = self.parent[e.fr]

        return path

    def distance_to(self, v):
        return self.dist[v]
