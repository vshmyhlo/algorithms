def depth_first_search(graph, v, visited, stack):
    visited[v] = True

    for w in graph.adjacent(v):
        if visited[w]:
            continue

        depth_first_search(graph, w, visited, stack)

    stack.append(v)


def topological_sort(graph):
    visited = [False] * graph.num_vertices
    stack = []

    for v in range(graph.num_vertices):
        if visited[v]:
            continue

        depth_first_search(graph, v, visited, stack)

    return reversed(stack)
