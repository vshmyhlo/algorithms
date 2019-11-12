from shuffle import shuffle


def three_way_quick_sort(seq):
    shuffle(seq)
    quick_subsort(seq, 0, len(seq))


def quick_subsort(seq, lo, hi):
    if hi - lo <= 1:
        return

    lt, gt = partition(seq, lo, hi)
    quick_subsort(seq, lo, lt)
    quick_subsort(seq, gt, hi)


def partition(seq, lo, hi):
    v = seq[lo]

    i = lo
    lt = lo
    gt = hi

    while i < gt:
        if seq[i] < v:
            swap(seq, i, lt)
            i += 1
            lt += 1
        elif v < seq[i]:
            swap(seq, i, gt - 1)
            gt -= 1
        else:
            i += 1

    return lt, gt


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
