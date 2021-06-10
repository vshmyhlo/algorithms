class Node(object):
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashMap(object):
    def __init__(self, buckets=256):
        self.buckets = [None for _ in range(buckets)]
        self.size = 0

    def __getitem__(self, key):
        node = self.buckets[self.key_to_index(key)]

        while node is not None:
            if node.key == key:
                return node.value

            node = node.next

        raise KeyError(key)

    def __setitem__(self, key, value):
        node = self.buckets[self.key_to_index(key)]

        while node is not None:
            if node.key == key:
                node.value = value
                return

            node = node.next

        self.buckets[self.key_to_index(key)] = Node(
            key, value, self.buckets[self.key_to_index(key)]
        )
        self.size += 1

    def __delitem__(self, key):
        node = self.buckets[self.key_to_index(key)]

        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.buckets[self.key_to_index(key)] = node.next
                else:
                    prev.next = node.next

                self.size -= 1
                return

            prev = node
            node = node.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        node = self.buckets[self.key_to_index(key)]

        while node is not None:
            if node.key == key:
                return True

            node = node.next

        return False

    def __iter__(self):
        for node in self.buckets:
            while node is not None:
                yield node.key

                node = node.next

    def key_to_index(self, key):
        return (hash(key) & 0x7FFFFFFF) % len(self.buckets)
