from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        approach
        recursion
        if root.val out of range, return 0 for this node
        else, we can prune
        if low > current val, just do the right
        if high < current val, just do the left
        else do both
        """

        def rangeSumBSTRecur(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            if root.val >= low and root.val <= high:
                return (
                    root.val
                    + rangeSumBSTRecur(root.left)
                    + rangeSumBSTRecur(root.right)
                )
            elif root.val < low:
                return rangeSumBSTRecur(root.right)
            elif root.val > high:
                return rangeSumBSTRecur(root.left)

        return rangeSumBSTRecur(root)
