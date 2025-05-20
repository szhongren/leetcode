from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        approach
        bfs
        put every child onto queue, then when I meet a None, I must not meet another node
        return True at the end
        """
        if root is None:
            return True
        queue = deque([root])
        at_end = False
        while queue:
            node = queue.popleft()
            if node is None:
                at_end = True
                continue
            # already seen a None but this is not None
            if at_end:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
