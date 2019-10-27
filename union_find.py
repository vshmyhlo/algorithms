# TODO: finish, move to graphs

class UnionFind(object):
    def __init__(self, size):
        self.id_to_parent = list(range(size))
        self.size = [1] * size

    def union(self, a, b):
        a = self.get_root(a)
        b = self.get_root(b)

        if self.size[a] < self.size[b]:
            self.id_to_parent[a] = b
            self.size[b] += self.size[a]
        else:
            self.id_to_parent[b] = a
            self.size[a] += self.size[b]

    def connected(self, a, b):
        return self.get_root(a) == self.get_root(b)

    def get_root(self, i):
        while self.id_to_parent[i] != i:
            i = self.id_to_parent[i]

        return i

# x = UnionFind(4)
# # x.union(0, 1)
# x.union(1, 0)
# x.union(2, 0)
# x.union(3, 0)
# # x.union(2, 3)
# # x.union(0, 2)
# print(x.size)
# print(x.id_to_parent)
