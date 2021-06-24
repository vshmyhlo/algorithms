def solution(input):
    max_diff = 0
    min_so_far = float("inf")

    for n in input:
        max_diff = max(max_diff, n - min_so_far)
        min_so_far = min(min_so_far, n)

    return max_diff


def test():
    input = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    expected = 30

    assert solution(input) == expected
