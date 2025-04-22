from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        approach
        naive:
        for each tree, get average, and check against current value
        need to return 2 things: total, and num of nodes
        """
        self.result = 0

        def averageOfSubtreeRecur(root: TreeNode) -> Tuple[int, int]:
            if root is None:
                return (0, 0)
            if root.left is None and root.right is None:
                self.result += 1
                return (root.val, 1)
            else:
                left_sum, left_count = averageOfSubtreeRecur(root.left)
                right_sum, right_count = averageOfSubtreeRecur(root.right)
                total = root.val + left_sum + right_sum
                total_count = 1 + left_count + right_count
                if int(total / total_count) == root.val:
                    self.result += 1
                return (total, total_count)

        averageOfSubtreeRecur(root)
        return self.result
