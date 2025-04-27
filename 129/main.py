from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        approach
        tail recursion
        for leaf node, return running sum
        else, add sum for each branch
        return sum
        """

        def sumNumbersRecur(root: Optional[TreeNode], running_sum: int) -> int:
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return running_sum * 10 + root.val
            else:
                return sumNumbersRecur(
                    root.left, running_sum * 10 + root.val
                ) + sumNumbersRecur(root.right, running_sum * 10 + root.val)

        return sumNumbersRecur(root, 0)
