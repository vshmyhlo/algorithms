# TODO:
# TODO: use linked list


class HashMap(object):
    def __init__(self, buckets=256):
        self.buckets = [[] for _ in range(buckets)]
        self.size = 0

    def __getitem__(self, key):
        bucket = self.buckets[self.key_to_index(key)]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __setitem__(self, key, value):
        bucket = self.buckets[self.key_to_index(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return

        bucket.append((key, value))
        self.size += 1

    def __delitem__(self, key):
        bucket = self.buckets[self.key_to_index(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        bucket = self.buckets[self.key_to_index(key)]

        for k, v in bucket:
            if k == key:
                return True

        return False

    def __iter__(self):
        for bucket in self.buckets:
            for k, _ in bucket:
                yield k

    def key_to_index(self, key):
        return (hash(key) & 0x7fffffff) % len(self.buckets)
