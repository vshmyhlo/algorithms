import numpy as np


def shuffle(xs):
    for i in range(len(xs)):
        j = np.random.randint(0, i + 1)
        xs[i], xs[j] = xs[j], xs[i]
