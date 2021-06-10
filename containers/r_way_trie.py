class Node(object):
    def __init__(self, key):
        self.key = key
        self.value = None
        self.children = [None] * 26


class RWayTrie(object):
    def __init__(self):
        self.root = Node("")

    def __getitem__(self, key):
        node = getitem(self.root, key, 0)

        if node is None:
            return None

        return node.value

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value, 0)

    def __delitem__(self, key):
        self.root = delitem(self.root, key, 0)

        if self.root is None:
            self.__init__()

    def __contains__(self, key):
        return self[key] is not None

    def __iter__(self):
        return iterate(self.root, "")


def getitem(node, key, depth):
    if node is None:
        return None

    if depth == len(key):
        return node
    else:
        i = index_of(key[depth])
        return getitem(node.children[i], key, depth + 1)


def setitem(node, key, value, depth):
    if node is None:
        node = Node(key[depth - 1])

    if depth == len(key):
        node.value = value
    else:
        i = index_of(key[depth])
        node.children[i] = setitem(node.children[i], key, value, depth + 1)

    return node


def delitem(node, key, depth):
    if node is None:
        return None

    if depth == len(key):
        node.value = None
    else:
        i = index_of(key[depth])
        node.children[i] = delitem(node.children[i], key, depth + 1)

    if node.value is None and all(child is None for child in node.children):
        return None

    return node


def iterate(node, prefix):
    if node is None:
        return

    if node.value is not None:
        yield prefix + node.key

    for child in node.children:
        yield from iterate(child, prefix + node.key)


def index_of(c):
    return ord(c) - ord("a")
