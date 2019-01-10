def insertion_sort(xs):
    xs = xs.copy()

    for i in range(1, len(xs)):
        for j in range(i, 0, -1):
            if xs[j - 1] > xs[j]:
                xs[j - 1], xs[j] = xs[j], xs[j - 1]
            else:
                break

    return xs
