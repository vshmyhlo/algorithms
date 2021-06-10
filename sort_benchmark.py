import time

import numpy as np

from shuffle import shuffle
from sorting.heap_sort import heap_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.selection_sort import selection_sort
from sorting.shell_sort import shell_sort

xs = list(np.random.randint(0, 10000, 10000))

for sort in [
    selection_sort,
    insertion_sort,
    shell_sort,
    merge_sort,
    quick_sort,
    heap_sort,
]:
    t = time.time()
    shuffle(xs)
    sort(xs)
    print("{} {:.4f}".format(sort.__name__, time.time() - t))
