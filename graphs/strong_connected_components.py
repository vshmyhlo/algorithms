from graphs.topological_sort import topological_sort


class StrongConnectedComponents(object):
    def __init__(self, graph):
        self.visited = [False] * graph.num_vertices
        self.id = [None] * graph.num_vertices
        self.size = 0

        order = topological_sort(graph.reverse())

        for v in order:
            if self.visited[v]:
                continue

            self.depth_first_search(graph, v)
            self.size += 1

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def component_id(self, v):
        return self.id[v]

    def __len__(self):
        return self.size

    def depth_first_search(self, graph, v):
        self.visited[v] = True
        self.id[v] = self.size

        for w in graph.adjacent(v):
            if self.visited[w]:
                continue

            self.depth_first_search(graph, w)
