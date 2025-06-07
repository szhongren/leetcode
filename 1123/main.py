from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        approach
        check depth of left and right subtrees, if they are the same, we are at the right lca
        else, return left or right
        """

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0, None
            left_depth, left_result = dfs(root.left)
            right_depth, right_result = dfs(root.right)

            if left_depth > right_depth:
                return left_depth + 1, left_result
            elif left_depth < right_depth:
                return right_depth + 1, right_result
            return left_depth + 1, root

        return dfs(root)[1]
