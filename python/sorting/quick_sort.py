import numpy as np


# TODO:
def quick_sort(xs):
    if len(xs) <= 1:
        return xs

    less = []
    greater = []
    equal = []
    pivot = xs[np.random.randint(len(xs))]

    for x in xs:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)

    xs = quick_sort(less) + equal + quick_sort(greater)

    return xs

# def sort(xs):
#     xs = xs.copy()
#
#     if len(xs) <= 1:
#         return xs
#
#     p = 0
#     for i in range(1, len(xs)):
#         if xs[i] < xs[p]:
#             xs[i], xs[p] = xs[p], xs[i]
#         p += 1
#
#     sort(xs[:p])
#     sort(xs[p + 1:])
#
#     return xs
