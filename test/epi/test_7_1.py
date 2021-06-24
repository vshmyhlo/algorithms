# from containers.linked_list import Node
#
#
# def solution(a, b):
#     max_diff = 0
#     min_so_far = float("inf")
#
#     for n in input:
#         max_diff = max(max_diff, n - min_so_far)
#         min_so_far = min(min_so_far, n)
#
#     return max_diff
#
#
# def test():
#     a = array_to_head([2, 4, 5, 6, 10])
#     b = array_to_head([0, 1, 3, 7, 8, 9])
#
#     assert solution(input) == expected
