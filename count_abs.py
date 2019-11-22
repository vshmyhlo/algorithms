def count_abs(seq, debug=False):
    if len(seq) == 0:
        return 0

    if len(seq) == 1:
        return 1

    seq = [abs(x) for x in seq]

    l = 0
    r = len(seq) - 1
    count = 0
    current = float('inf')

    while l <= r:
        if debug:
            debug_count_abs(seq, count, current, l, r)

        if seq[l] < seq[r]:
            if current != seq[r]:
                count += 1
                current = seq[r]

            r -= 1
        elif seq[l] > seq[r]:
            if current != seq[l]:
                count += 1
                current = seq[l]

            l += 1
        else:
            r -= 1

    if current != seq[l]:
        count += 1

    return count


def debug_count_abs(seq, count, current, l, r):
    print('{} | {} | [{}]'.format(
        count,
        current,
        ','.join(
            '[{}]'.format(x) if i == l or i == r else ' {} '.format(x)
            for i, x in enumerate(seq))))
