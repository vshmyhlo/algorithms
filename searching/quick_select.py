from shuffle import shuffle
from sorting.quick_sort import partition


def quick_select(seq, k):
    assert len(seq) > 0

    shuffle(seq)

    lo = 0
    hi = len(seq)

    while lo < hi:
        j = partition(seq, lo, hi)

        if k < j:
            hi = j
        elif j < k:
            lo = j + 1
        else:
            return seq[j]

    return seq[k]
