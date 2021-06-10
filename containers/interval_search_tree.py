class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.max = key[1]
        self.left = None
        self.right = None


class IntervalSearchTree(object):
    def __init__(self):
        self.root = None

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value)

    def intersection_search(self, key):
        return intersection_search(self.root, key)


def setitem(node, key, value):
    if node is None:
        return Node(key, value)

    if key[0] < node.key[0]:
        node.left = setitem(node.left, key, value)
        node.max = max(node.max, node.left.max)
    elif node.key[0] < key[0]:
        node.right = setitem(node.right, key, value)
        node.max = max(node.max, node.right.max)
    else:
        raise NotImplementedError()

    return node


def intersection_search(node, key):
    if node is None:
        return None

    if intersects(node.key, key):
        return node.key
    elif node.left is None:
        return intersection_search(node.right, key)
    elif node.left.max < key[0]:
        return intersection_search(node.right, key)
    else:
        return intersection_search(node.left, key)


def intersects(a, b):
    return a[0] <= b[0] < a[1] or a[0] < b[1] <= a[1]
