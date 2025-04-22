from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        approach
        binary search and for each node, check to see if it's closer
        """
        self.closest = inf

        def closestValueRecur(root: Optional[TreeNode]):
            if root is None:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val
            if abs(root.val - target) == abs(self.closest - target):
                self.closest = min(root.val, self.closest)
            if target < root.val:
                closestValueRecur(root.left)
            else:
                closestValueRecur(root.right)

        closestValueRecur(root)

        return self.closest
