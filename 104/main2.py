# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_recursive(root, 0)

    def max_depth_recursive(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth
        return max(
            self.max_depth_recursive(root.left, depth + 1),
            self.max_depth_recursive(root.right, depth + 1),
        )
