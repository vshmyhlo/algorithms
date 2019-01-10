import numpy as np


def shuffle(xs):
    xs = xs.copy()

    for i in range(len(xs)):
        j = np.random.randint(0, i + 1)
        xs[i], xs[j] = xs[j], xs[i]

    return xs
