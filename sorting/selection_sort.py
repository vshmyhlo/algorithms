# def selection_sort(xs):
#     xs = xs.copy()
#
#     for i in range(len(xs)):
#         for j in range(i + 1, len(xs)):
#             if xs[i] > xs[j]:
#                 xs[i], xs[j] = xs[j], xs[i]
#
#     return xs


def selection_sort(xs):
    xs = xs.copy()

    for i in range(len(xs)):
        min = i
        for j in range(i + 1, len(xs)):
            if xs[min] > xs[j]:
                min = j
        xs[i], xs[min] = xs[min], xs[i]

    return xs
