from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def longestZigZagRecur(
            root: Optional[TreeNode], inPath: bool, goRight: bool, curr_len: int
        ) -> int:
            if root is None:
                return
            nonlocal max_length
            max_length = max(max_length, curr_len)
            if inPath:
                longestZigZagRecur(
                    root.right if goRight else root.left,
                    True,
                    not goRight,
                    curr_len + 1,
                )
            else:
                longestZigZagRecur(root.left, False, True, curr_len)
                longestZigZagRecur(root.right, False, False, curr_len)
                longestZigZagRecur(root.left, True, True, curr_len + 1)
                longestZigZagRecur(root.right, True, False, curr_len + 1)

        def longestZigZagRecur2(
            self, root: Optional[TreeNode], go_right: bool, curr_len: int
        ) -> int:
            if root is None:
                return
            nonlocal max_length
            max_length = max(max_length, curr_len)
            if go_right:
                longestZigZagRecur2(root.right, False, curr_len + 1)
                longestZigZagRecur2(root.left, True, 1)
            else:
                longestZigZagRecur2(root.left, True, curr_len + 1)
                longestZigZagRecur2(root.right, False, 1)

        if root.left is not None or root.right is not None:
            # longestZigZagRecur(root, True, True, 0)
            # longestZigZagRecur(root, True, False, 0)
            # longestZigZagRecur(root, False, True, 0)
            # longestZigZagRecur(root, False, False, 0)
            longestZigZagRecur2(root, True, 0)
            longestZigZagRecur2(root, False, 0)
        return max_length
