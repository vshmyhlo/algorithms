import random

from containers.priority_queue import PriorityQueue


def solution(lists):
    q = PriorityQueue()
    result = []

    for li, l in enumerate(lists):
        q.push((l[0], 0, li))

    while q:
        x, xi, li = q.pop_min()
        result.append(x)

        if xi + 1 < len(lists[li]):
            q.push((lists[li][xi + 1], xi + 1, li))

    return result


def test_solution():
    lists = [sorted(random.randint(0, 100) for _ in range(100)) for _ in range(50)]
    actual = solution(lists)

    expected = []
    for l in lists:
        expected.extend(l)
    expected.sort()

    assert actual == expected
