import math
import os
from multiprocessing import Pool

from sorting.merge_sort import merge as basic_merge


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

        (seq,) = chunks

        return seq


def merge(left_right):
    left, right = left_right

    if right is None:
        return left

    return basic_merge(left, right)
