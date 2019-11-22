import numpy as np


def is_sym(ps):
    if len(ps) == 0:
        return True

    mid = np.mean(ps[:, 0])

    left = ps[ps[:, 0] < mid]
    right = ps[ps[:, 0] > mid]

    left = np.sort(left, axis=0, kind='stable')
    right = np.sort(right, axis=0, kind='stable')

    left[:, 0] = mid - left[:, 0]
    right[:, 0] = right[:, 0] - mid

    return np.array_equal(left, right)
