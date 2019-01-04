# TODO:


class HashMap(object):
    def __init__(self, buckets=16):
        self.buckets = [[] for _ in range(buckets)]
        self.size = 0

    def __getitem__(self, key):
        h = hash(key)
        bucket = self.buckets[h % len(self.buckets)]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __setitem__(self, key, value):
        h = hash(key)
        bucket = self.buckets[h % len(self.buckets)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return

        bucket.append((key, value))
        self.size += 1

    def __delitem__(self, key):
        h = hash(key)
        bucket = self.buckets[h % len(self.buckets)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        h = hash(key)
        bucket = self.buckets[h % len(self.buckets)]

        for k, v in bucket:
            if k == key:
                return True

        return False


