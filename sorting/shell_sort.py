def insertion_sort(xs, stride):
    for i in range(stride, len(xs)):
        for j in range(i, 0, -stride):
            if xs[j - stride] > xs[j]:
                xs[j - stride], xs[j] = xs[j], xs[j - stride]
            else:
                break


# TODO:
def shell_sort(xs):
    stride = 1
    strides = []
    while stride < len(xs) // 3:
        strides.append(stride)
        stride = stride * 3 + 1
    strides = list(reversed(strides))

    for stride in strides:
        insertion_sort(xs, stride)
