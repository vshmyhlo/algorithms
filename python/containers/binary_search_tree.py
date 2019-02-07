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


def setitem(root, key, value):
    if root is None:
        return Node(key, value)

    if key < root.key:
        root.left = setitem(root.left, key, value)
    elif key > root.key:
        root.right = setitem(root.right, key, value)
    else:
        root.value = value

    root.size = 1 + size(root.left) + size(root.right)

    return root


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
