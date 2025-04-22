from collections import deque
from typing import Optional, List


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
        use a queue
        for each iteration, take queue[-1] to be the rightmost
        then, for each item in the queue, put its children onto the queue, left then right
        end when no items in the queue
        """
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                # remove items from this level
                item = queue.popleft()
                # add the next
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)
        return result
