import numpy as np


def sort(xs):
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

    xs = sort(less) + equal + sort(greater)

    return xs
