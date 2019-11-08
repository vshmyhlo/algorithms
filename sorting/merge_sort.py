def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    seq = merge(left, right)

    return seq


def merge(left, right):
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
