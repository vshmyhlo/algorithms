from shuffle import shuffle


# TODO:
def quick_sort(xs):
    shuffle(xs)
    quick_subsort(xs, 0, len(xs))


def quick_subsort(xs, lo, hi):
    if hi - lo <= 1:
        return

    mid = partition(xs, lo, hi)
    quick_subsort(xs, lo, mid)
    quick_subsort(xs, mid + 1, hi)


def partition(xs, lo, hi):
    p = xs[lo]
    l = lo + 1
    r = hi - 1

    while True:
        while xs[l] <= p and l != hi - 1:
            l += 1

        while p <= xs[r] and r != lo:
            r -= 1

        if l >= r:
            break

        xs[l], xs[r] = xs[r], xs[l]

    xs[lo], xs[r] = xs[r], xs[lo]

    return r
