from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        """
        approach
        recursive
        if arr is empty, return if root is None
        else, if root.val == arr[0], return if any(recur(root.left), recur(root.right))
        """
        if root is None:
            return len(arr) == 0

        def isLeaf(root: Optional[TreeNode]):
            if root is None:
                return False
            return root.left is None and root.right is None

        def isValidSequenceRecur(root: Optional[TreeNode], arr: List[int]) -> bool:
            if isLeaf(root):
                return len(arr) == 1 and arr[0] == root.val
            if root is None:
                return False
            if len(arr) == 0:
                return False
            if root.val != arr[0]:
                return False
            return any(
                [
                    isValidSequenceRecur(root.left, arr[1:]),
                    isValidSequenceRecur(root.right, arr[1:]),
                ]
            )

        return isValidSequenceRecur(root, arr)
