"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(ls):
    """
    :type ls: List[int]
    :rtype: TreeNode
    """
    if len(ls) == 0:
        return None
    list_nodes = list(map(lambda x: TreeNode(x) if x != None else None, ls))
    length = len(list_nodes)
    for i in range(length // 2):
        if list_nodes[i] != None:
            if i * 2 + 1 < length:
                list_nodes[i].left = list_nodes[i * 2 + 1]
            if i * 2 + 2 < length:
                list_nodes[i].right = list_nodes[i * 2 + 2]
    return list_nodes[0]

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         if root == None:
#             return '#'
#         return '[' + self.serialize(root.left) + str(root.val) + self.serialize(root.right) + ']'

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         length = len(data)
#         if length == 1 and data == '#':
#             return None
#         paren_counts = [0 for _ in range(length + 1)]
#         paren_counts[1] = 1
#         start = 2
#         for i in range(2, length + 1):
#             paren_counts[i] = paren_counts[i - 1]
#             if data[i - 1] == '[':
#                 paren_counts[i] += 1
#             if data[i - 1] == ']':
#                 paren_counts[i] += -1
#             if paren_counts[i] == 1:
#                 start = i
#                 break
#         paren_counts[-2] = 1
#         end = length - 2
#         for i in range(length - 2, -1, -1):
#             paren_counts[i] = paren_counts[i + 1]
#             if data[i] == ']':
#                 paren_counts[i] += 1
#             if data[i] == '[':
#                 paren_counts[i] += -1
#             if paren_counts[i] == 1:
#                 end = i
#                 break
#         out = TreeNode(int(data[start:end]))
#         out.left = self.deserialize(data[1:start])
#         out.right = self.deserialize(data[end:-1])
#         return out

class Codec:
    # preorder serialization
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

codec = Codec()
print(codec.serialize(codec.deserialize(codec.serialize(make_tree([1, 2, 3, 4, None, None, 5])))))
print(codec.serialize(make_tree([1, 2, 3, 4, None, None, 5])))

