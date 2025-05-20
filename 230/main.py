from typing import Optional
from heapq import heappush, heappop


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        approach
        use a heap, push every element onto it
        if size of heap > k, pop
        use a max heap
        """
        self.heap = []

        def kthSmallestRecur(root: Optional[TreeNode]):
            if root is None:
                return
            heappush(self.heap, -root.val)
            if len(self.heap) > k:
                heappop(self.heap)
            kthSmallestRecur(root.left)
            kthSmallestRecur(root.right)

        kthSmallestRecur(root)
        return -self.heap[0]
