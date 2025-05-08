from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        approach
        recursive
        each call should return f"{root.val}({recur(root.left)})({recur(root.right)})"
        if None, return ""
        wrap child in parents if not empty string
        """

        def tree2str_recur(root: Optional[TreeNode]):
            if root is None:
                return ""
            left_str = tree2str_recur(root.left)
            right_str = tree2str_recur(root.right)
            if not left_str and not right_str:
                return f"{root.val}"
            if not left_str and right_str:
                return f"{root.val}()({right_str})"
            if left_str and not right_str:
                return f"{root.val}({left_str})"
            if left_str and right_str:
                return f"{root.val}({left_str})({right_str})"

        return tree2str_recur(root)
