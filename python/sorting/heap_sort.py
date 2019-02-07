# TODO: separate inplace from not inplace algorithms
# TODO: index arithmetic (start from 1)

def heap_sort(xs):
    xs = xs.copy()
    xs.insert(0, None)
    construct(xs)
    sort(xs)
    xs = xs[1:]

    return xs


def construct(xs):
    n = len(xs)
    for i in range(n // 2, 0, -1):
        sink(xs, i, n)


def sort(xs):
    n = len(xs)
    for i in range(n - 1, 0, -1):
        xs[1], xs[i] = xs[i], xs[1]
        sink(xs, 1, i)


def sink(xs, i, n):
    while i * 2 < n:
        j = i * 2

        if j + 1 < n and xs[j] < xs[j + 1]:
            j += 1

        if xs[i] < xs[j]:
            xs[i], xs[j] = xs[j], xs[i]
        else:
            break

        i = j
