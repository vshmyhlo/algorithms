import matplotlib.pyplot as plt
import numpy as np


# TODO:
# def ccw(a, b, c):
#     ba = (b[1] - a[1]) / (b[0] - a[0])
#     ca = (c[1] - a[1]) / (c[0] - a[0])
#
#     return ca > ba

def ccw(a, b, c):
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    return area > 0


def graham_scan(points):
    points = points[np.argsort(points[:, 0])]
    p, points = points[0], points[1:]
    slope = (points[:, 1] - p[1]) / (points[:, 0] - p[0])
    points = points[np.argsort(slope)]

    hull = [p, points[0]]
    for c in points[1:]:
        b = hull.pop()
        a = hull.pop()

        while not ccw(a, b, c):
            hull.append(a)
            b = hull.pop()
            a = hull.pop()

        hull.extend([a, b, c])

    return hull


points = np.random.standard_normal(size=[100, 2])
hull = graham_scan(points)

plt.scatter(points[:, 0], points[:, 1], s=5)
for i in range(1, len(hull)):
    plt.arrow(*hull[i - 1], *hull[i] - hull[i - 1])
plt.arrow(*hull[-1], *hull[0] - hull[-1])
plt.show()
