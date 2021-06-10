class Node(object):
    def __init__(self, key):
        self.key = key
        self.value = None
        self.left = None
        self.mid = None
        self.right = None


class TernaryTrie(object):
    def __init__(self):
        self.root = None

    def __getitem__(self, key):
        node = getitem(self.root, key, 0)

        if node is None:
            return None

        return node.value

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value, 0)

    def __delitem__(self, key):
        self.root = delitem(self.root, key, 0)

    def __contains__(self, key):
        return self[key] is not None

    def __iter__(self):
        return iterate(self.root, "")

    def keys_with_prefix(self, prefix):
        node = getitem(self.root, prefix, 0)

        if node is None:
            return

        if node.value is not None:
            yield prefix

        yield from iterate(node.mid, prefix)

    def longest_prefix_of(self, query):
        i = find_index(self.root, query, 0, 0)

        return query[:i]


def getitem(node, key, depth):
    if node is None:
        return None

    if key[depth] < node.key:
        return getitem(node.left, key, depth)
    elif node.key < key[depth]:
        return getitem(node.right, key, depth)
    elif depth == len(key) - 1:
        return node
    else:
        return getitem(node.mid, key, depth + 1)


def setitem(node, key, value, depth):
    if node is None:
        node = Node(key[depth])

    if key[depth] < node.key:
        node.left = setitem(node.left, key, value, depth)
    elif node.key < key[depth]:
        node.right = setitem(node.right, key, value, depth)
    elif depth == len(key) - 1:
        node.value = value
    else:
        node.mid = setitem(node.mid, key, value, depth + 1)

    return node


def delitem(node, key, depth):
    if node is None:
        return None

    if key[depth] < node.key:
        node.left = delitem(node.left, key, depth)
    elif node.key < key[depth]:
        node.right = delitem(node.right, key, depth)
    elif depth == len(key) - 1:
        node.value = None
    else:
        node.mid = delitem(node.mid, key, depth + 1)

    if (
        node.value is None
        and node.left is None
        and node.mid is None
        and node.right is None
    ):
        return None

    return node


def iterate(node, prefix):
    if node is None:
        return

    yield from iterate(node.left, prefix)

    if node.value is not None:
        yield prefix + node.key
    yield from iterate(node.mid, prefix + node.key)

    yield from iterate(node.right, prefix)


def find_index(node, query, length, depth):
    if node is None:
        return length

    if query[depth] < node.key:
        return find_index(node.left, query, length, depth)
    elif node.key < query[depth]:
        return find_index(node.right, query, length, depth)
    else:
        if node.value is not None:
            length = depth + 1

        return find_index(node.mid, query, length, depth + 1)
