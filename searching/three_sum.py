from searching.binary_search import binary_search


# TODO:  find better than simple brute force


def three_sum(xs):
    xs = sorted(xs)
    size = len(xs)
    result = 0

    for i in range(size):
        for j in range(i + 1, size):
            # # TODO: checks only first matching number
            # index = binary_search(xs[j + 1:], -(xs[i] + xs[j]))
            # if index is not None:
            #     result += 1

            for k in range(j + 1, size):
                if -(xs[i] + xs[j]) == xs[k]:
                    result += 1

    # for values in itertools.combinations(xs, 2):
    #     index = binary_search(xs, -sum(values))
    #     if index is not None:
    #         result += 1

    # for i in range(size):
    #     for j in range(i + 1, size):
    #         for k in range(j + 1, size):
    #             if xs[i] + xs[j] + xs[k] == 0:
    #                 result += 1

    return result
