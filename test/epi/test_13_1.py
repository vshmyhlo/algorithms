import random


def solution(a, b):
    result = []
    ai = 0
    bi = 0
    last = None

    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            ai += 1
        elif b[bi] < a[ai]:
            bi += 1
        else:
            if last != a[ai]:
                last = a[ai]
                result.append(last)
            ai += 1
            bi += 1

    return result


def test_solution():
    a = sorted(random.randint(0, 10) for _ in range(100))
    b = sorted(random.randint(5, 15) for _ in range(100))

    expected = sorted(set(a).intersection(set(b)))
    actual = solution(a, b)

    assert actual == expected
