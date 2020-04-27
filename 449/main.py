"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serializeRecur(node, level):
            if node == None:
                return '#'
            next_level = chr(ord(level) + 1)
            return serializeRecur(node.left, next_level) + level + str(node.val) + level + serializeRecur(node.right, next_level)
        return serializeRecur(root, 'A')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeRecur(code, level):
            if len(code) == 1 and code == '#':
                return None
            next_level = chr(ord(level) + 1)
            start = code.find(level)
            end = code.rfind(level)
            out = TreeNode(int(code[start + 1: end]))
            out.left = deserializeRecur(code[:start], next_level)
            out.right = deserializeRecur(code[end + 1:], next_level)
            return out
        return deserializeRecur(data, 'A')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
codec = Codec()
print(codec.serialize(codec.deserialize(codec.serialize(make_tree([1, 2, 3, 4, None, None, 5])))))
print(codec.serialize(make_tree([1, 2, 3, 4, None, None, 5])))
