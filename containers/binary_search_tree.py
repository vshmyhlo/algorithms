# TODO: meaningful method names in all classes
# TODO: implement all methods mentioned


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def __iter__(self):
        if self.left is not None:
            yield from self.left

        yield self.key

        if self.right is not None:
            yield from self.right


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        self.root = setitem(self.root, key, value)

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

    def __delitem__(self, key):
        self.root, found = delitem(self.root, key)

        if not found:
            raise KeyError(key)

    def __len__(self):
        return size(self.root)

    def __iter__(self):
        if self.root is not None:
            yield from self.root

    def __contains__(self, key):
        root = self.root

        while root is not None:
            if key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                return True

        return False

    def min(self):
        root = self.root

        if root is None:
            raise ValueError('min of empty {}'.format(self.__class__.__name__))

        while root.left is not None:
            root = root.left

        return root.key

    def max(self):
        root = self.root

        if root is None:
            raise ValueError('max of empty {}'.format(self.__class__.__name__))

        while root.right is not None:
            root = root.right

        return root.key

    def delete_min(self):
        if self.root is None:
            raise ValueError('delete_min of empty {}'.format(self.__class__.__name__))

        self.root = delete_min(self.root)

    def delete_max(self):
        if self.root is None:
            raise ValueError('delete_max of empty {}'.format(self.__class__.__name__))

        self.root = delete_max(self.root)

    def floor(self, key):
        node, found = floor(self.root, key)

        if not found:
            raise ValueError('floor is outside of {}'.format(self.__class__.__name__))

        return node.key

    def ceil(self, key):
        node, found = ceil(self.root, key)

        if not found:
            raise ValueError('ceil is outside of {}'.format(self.__class__.__name__))

        return node.key

    def rank(self, key):
        return rank(self.root, key)

    def select(self, key):
        raise NotImplementedError()

    def range_count(self, lo, hi):
        if hi in self:
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def range_search(self, lo, hi):
        yield from range_search(self.root, lo, hi)


def setitem(node, key, value):
    if node is None:
        return Node(key, value)

    if key < node.key:
        node.left = setitem(node.left, key, value)
    elif key > node.key:
        node.right = setitem(node.right, key, value)
    else:
        node.value = value

    node.size = 1 + size(node.left) + size(node.right)

    return node


def delitem(root, key):
    if root is None:
        return root, False

    if key < root.key:
        root.left, found = delitem(root.left, key)
    elif key > root.key:
        root.right, found = delitem(root.right, key)
    else:
        if root.left is None:
            root, found = root.right, True
        elif root.right is None:
            root, found = root.left, True
        else:
            min = root.right
            while min.left is not None:
                min = min.left

            min.right = delete_min(root.right)
            min.left = root.left
            root, found = min, True

    root.size = 1 + size(root.left) + size(root.right)

    return root, found


def floor(root, key):
    if root is None:
        return root, False

    if key < root.key:
        return floor(root.left, key)
    elif key > root.key:
        node, found = floor(root.right, key)

        if found:
            return node, True
        else:
            return root, True
    else:
        return root, True


def ceil(root, key):
    if root is None:
        return root, False

    if key > root.key:
        return ceil(root.right, key)
    elif key < root.key:
        node, found = ceil(root.left, key)

        if found:
            return node, True
        else:
            return root, True
    else:
        return root, True


def size(root):
    if root is None:
        return 0
    else:
        return root.size


def rank(root, key):
    if root is None:
        return 0

    if key < root.key:
        return rank(root.left, key)
    elif key > root.key:
        return 1 + size(root.left) + rank(root.right, key)
    else:
        return size(root.left)


def delete_min(root):
    if root.left is None:
        return root.right

    root.left = delete_min(root.left)
    root.size = 1 + size(root.left) + size(root.right)

    return root


def delete_max(root):
    if root.right is None:
        return root.left

    root.right = delete_max(root.right)
    root.size = 1 + size(root.left) + size(root.right)

    return root


def range_search(node, lo, hi):
    if node is None:
        return

    if lo <= node.key:
        yield from range_search(node.left, lo, hi)

    if lo <= node.key <= hi:
        yield node.key

    if node.key <= hi:
        yield from range_search(node.right, lo, hi)
