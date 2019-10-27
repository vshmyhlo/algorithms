def binary_search(xs, x):
    return binary_subsearch(xs, x, 0, len(xs))


def binary_subsearch(xs, x, lo, hi):
    if hi - lo == 0:
        return None

    mid = lo + (hi - lo) // 2

    if x < xs[mid]:
        return binary_subsearch(xs, x, lo, mid)
    elif x > xs[mid]:
        return binary_subsearch(xs, x, mid + 1, hi)
    else:
        return mid
