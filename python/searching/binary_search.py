def binary_search(xs, x):
    return lo_hi_binary_search(xs, x, 0, len(xs))


def lo_hi_binary_search(xs, x, lo, hi):
    if hi - lo == 0:
        return None

    mid = lo + (hi - lo) // 2

    if x < xs[mid]:
        return lo_hi_binary_search(xs, x, lo, mid)
    elif x > xs[mid]:
        return lo_hi_binary_search(xs, x, mid + 1, hi)
    else:
        return mid
