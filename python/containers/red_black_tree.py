class Node(object):
    def __init__(self, key, value, is_red):
        self.key = key
        self.value = value
        self.is_red = is_red
        self.left = None
        self.right = None
        self.size = 1

    def rotate_left(self):
        assert is_red(self.right)

        right = self.right
        self.right = right.left
        right.left = self
        right.is_red = self.is_red
        self.is_red = True

        return right

    def rotate_right(self):
        assert is_red(self.left)

        left = self.left
        self.left = left.right
        left.right = self
        left.is_red = self.is_red
        self.is_red = True

        return left

    def flip_colors(self):
        assert is_black(self)
        assert is_red(self.left)
        assert is_red(self.right)

        self.is_red = True
        self.left.is_red = False
        self.right.is_red = False

        return self

    def __iter__(self):
        if self.left is not None:
            yield from self.left

        yield self.key

        if self.right is not None:
            yield from self.right


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def __getitem__(self, key):
        root = self.root

        while root is not None:
            if key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                return root.value

        raise KeyError(key)

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value)
        self.root.is_red = False

    def __iter__(self):
        if self.root is not None:
            yield from self.root

    def __len__(self):
        return size(self.root)


def is_red(node):
    if node is None:
        return False

    return node.is_red


def is_black(node):
    return not is_red(node)


def setitem(node, key, value):
    if node is None:
        return Node(key, value, is_red=True)

    if key < node.key:
        node.left = setitem(node.left, key, value)
    elif key > node.key:
        node.right = setitem(node.right, key, value)
    else:
        node.value = value

    if is_black(node.left) and is_red(node.right):
        node = node.rotate_left()
    if is_red(node.left) and is_red(node.left.left):
        node = node.rotate_right()
    if is_red(node.left) and is_red(node.right):
        node = node.flip_colors()

    node.size = 1 + size(node.left) + size(node.right)

    return node


def size(node):
    if node is None:
        return 0

    return node.size
