from containers.queue import LinkedListQueue as Queue


class BreadthFirstSearch(object):
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        self.edge_to = [None] * graph.num_vertices
        self.dist_to = [None] * graph.num_vertices

        self.breadth_first_search(graph, source)

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

    def distance_to(self, v):
        return self.dist_to[v]

    def breadth_first_search(self, graph, source):
        self.dist_to[source] = 0

        queue = Queue()
        queue.enqueue(source)

        while len(queue) > 0:
            v = queue.dequeue()
            self.visited[v] = True

            for w in graph.adjacent(v):
                if self.visited[w]:
                    continue

                self.edge_to[w] = v
                self.dist_to[w] = self.dist_to[v] + 1

                queue.enqueue(w)
