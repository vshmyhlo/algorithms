# KeyValue = collections.namedtuple('KeyValue', ['key', 'value'])
#
#
# class TwoNode(object):
#     def __init__(self, key_value):
#         self.key_value = key_value
#         self.children = None
#         self.size = 1
#
#     def add(self, key_value):
#         if self.children is None:
#             return ThreeNode(...)
#         else:
#             if self.k


# class ThreeNode(object):
#     def __init__(self, left_key, right_key):
#         pass


class TwoThreeTree(object):
    def __init__(self):
        self.root = None

    # def __setitem__(self, key, value):
    #     setitem
    #     # key_value = KeyValue(key=key, value=value)
    #
    # def __getitem__(self, key):
    #     pass

# def setitem(root, key, value):
# if root.is_three_node():
#     pass
#
# # if root.is_two_node():
# #     if key < root.key:
# #         setitem(root.left, key, value)
# #     if key > root.key:
# #         setitem(root.right, key, value)
# #     else:
# #         root.value = value
# # else:
# #     pass
