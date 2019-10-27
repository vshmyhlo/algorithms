# TODO: delete
# TODO: range_count

class Node(object):
    def __init__(self, key, value, k):
        self.key = key
        self.value = value
        self.k = k
        self.left = None
        self.right = None


class KDTree(object):
    def __init__(self, k):
        self.k = k
        self.root = None

    def __getitem__(self, key):
        return getitem(self.root, key)

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value, 0, self.k)

    def __contains__(self, key):
        return self[key] is not None

    def range_search(self, lo, hi):
        yield from range_search(self.root, lo, hi, self.k)


def getitem(node, key):
    if node is None:
        return None

    if node.key == key:
        return node.value

    if key[node.k] < node.key[node.k]:
        return getitem(node.left, key)
    else:
        return getitem(node.right, key)


def setitem(node, key, value, k, k_max):
    if node is None:
        return Node(key, value, k)
    assert node.k == k
    del k

    if node.key == key:
        node.value = value
        return node

    if key[node.k] < node.key[node.k]:
        node.left = setitem(node.left, key, value, (node.k + 1) % k_max, k_max)
    else:
        node.right = setitem(node.right, key, value, (node.k + 1) % k_max, k_max)

    return node


def range_search(node, lo, hi, k_max):
    if node is None:
        return

    if lo[node.k] <= node.key[node.k]:
        yield from range_search(node.left, lo, hi, k_max)

    inside = True
    for i in range(k_max):
        inside = inside and lo[i] <= node.key[i] <= hi[i]
        if not inside:
            break
    if inside:
        yield node.key

    if node.key[node.k] <= hi[node.k]:
        yield from range_search(node.right, lo, hi, k_max)
