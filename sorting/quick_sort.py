from shuffle import shuffle


def quick_sort(seq):
    shuffle(seq)
    quick_subsort(seq, 0, len(seq))


def quick_subsort(seq, lo, hi):
    if hi - lo <= 1:
        return

    mid = partition(seq, lo, hi)
    quick_subsort(seq, lo, mid)
    quick_subsort(seq, mid + 1, hi)


# TODO: check partition
def partition(seq, lo, hi):
    k = lo
    i = lo + 1
    j = hi - 1

    while True:
        while seq[i] < seq[k] and i < hi - 1:
            i += 1

        while seq[k] <= seq[j] and lo < j:
            j -= 1

        if j <= i:
            break

        swap(seq, i, j)

    swap(seq, j, k)

    return j


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
