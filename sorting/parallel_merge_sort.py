import math
import os
from multiprocessing import Pool


def group_chunks(chunks, num_chunks):
    for i in range(0, num_chunks, 2):
        yield (next(chunks), next(chunks) if i + 1 < num_chunks else None)


def parallel_merge_sort(seq, num_workers=os.cpu_count()):
    with Pool(num_workers) as pool:
        num_chunks = len(seq)
        chunks = ([n] for n in seq)

        while num_chunks > 1:
            chunks = group_chunks(chunks, num_chunks)
            chunks = pool.imap(merge, chunks)
            num_chunks = math.ceil(num_chunks / 2)

        seq, = chunks

        return seq


def merge(left_right):
    left, right = left_right

    if right is None:
        return left

    seq = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            seq.append(left[l])
            l += 1
        else:
            seq.append(right[r])
            r += 1

    seq.extend(left[l:])
    seq.extend(right[r:])

    return seq
