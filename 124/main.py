from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        to solve this problem, we have 2 basic cases
        1. case where the max path is in the left subtree entirely, or in the right subtree entirely
        2. case where the max path goes through the root node
        in case one, we just have to compare the max of left subtree recursive call and right subtree recursive call
        in case 2. we have to get the max sum to root of left and right, and add root.val to that, and compare that to the max of the left and max of the right
        then, add the edge cases of paths that don't go to a leaf
        edge cases:
        -1000
        100, 200
        """

        def maxPathSumToLeafWithEarlyStop(root: Optional[TreeNode]):
            if root is None:
                return -inf
            if root.left is None and root.right is None:
                return root.val
            left_sum = maxPathSumToLeafWithEarlyStop(root.left)
            right_sum = maxPathSumToLeafWithEarlyStop(root.right)
            return max(root.val, root.val + left_sum, root.val + right_sum)

        def maxPathSumRecur(root: Optional[TreeNode]):
            if root is None:
                return -inf
            left_path_sum = maxPathSumToLeafWithEarlyStop(root.left)
            right_path_sum = maxPathSumToLeafWithEarlyStop(root.right)  # -700
            return max(
                [
                    root.val + left_path_sum + right_path_sum,
                    left_path_sum,
                    right_path_sum,
                    root.val + left_path_sum,
                    root.val + right_path_sum,
                    maxPathSumRecur(root.left),
                    maxPathSumRecur(root.right),
                ]
            )

        return maxPathSumRecur(root)
