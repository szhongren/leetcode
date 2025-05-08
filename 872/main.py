from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        approach
        get leaf sequence
        compare
        get leaf sequence is easy, each recursive call should return [val] if leaf, otherwise concat left and right recursive lists
        """

        def leaf_sequence_recur(root: Optional[TreeNode]):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            left = leaf_sequence_recur(root.left)
            right = leaf_sequence_recur(root.right)
            return left + right

        a = leaf_sequence_recur(root1)
        b = leaf_sequence_recur(root2)
        if len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if x != y:
                return False
        return True
