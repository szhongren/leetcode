from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        approach
        for every level, put onto new queue
        result.append(queue[-1])
        queue = new_queue
        end when queue empty
        """
        result = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            result.append(queue[-1].val)
            new_queue = deque()
            for node in queue:
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)
            queue = new_queue
        return result
