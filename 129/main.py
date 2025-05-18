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
        recursive sum from the root
        each call carries a running sum
        for each node, if leaf, return accumulator
        otherwise, sum recur(children)
        edge cases
        None: + return
        if leaf, return acc
        """

        def sumNumbersRecur(root: Optional[TreeNode], acc: int) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return acc + root.val
            acc = acc + root.val
            return sum(
                [
                    sumNumbersRecur(root.left, acc * 10),
                    sumNumbersRecur(root.right, acc * 10),
                ]
            )

        return sumNumbersRecur(root, 0)
