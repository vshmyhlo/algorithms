def merge_sort(xs):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    xs = merge(left, right)

    return xs


def merge(left, right):
    xs = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            xs.append(left[l])
            l += 1
        else:
            xs.append(right[r])
            r += 1

    xs.extend(left[l:])
    xs.extend(right[r:])

    return xs
