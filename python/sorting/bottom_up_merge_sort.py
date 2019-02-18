def bottom_up_merge_sort(xs):
    window = 1
    size = len(xs)
    aux = xs.copy()

    while window < size:
        for lo in range(0, size - window, window * 2):
            mid = lo + window
            hi = min(lo + window * 2, size)
            merge(xs, aux, lo, mid, hi)

        window *= 2


def merge(xs, aux, lo, mid, hi):
    aux[lo:hi] = xs[lo:hi]

    l = lo
    r = mid
    i = lo

    while l < mid and r < hi:
        if aux[l] < aux[r]:
            xs[i] = aux[l]
            l += 1
        else:
            xs[i] = aux[r]
            r += 1

        i += 1

    while l < mid:
        xs[i] = aux[l]
        l += 1
        i += 1

    while r < hi:
        xs[i] = aux[r]
        r += 1
        i += 1
