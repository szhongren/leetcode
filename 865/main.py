from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        approach
        find all deepest nodes
        find lowest child
        recurse from the root until either leaf or left and right both have at least 1 deepest
        """
        deepest_nodes = set()
        queue = deque([root])
        while queue:
            deepest_nodes = set(queue)
            new_level = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if not new_level:
                break
            queue = new_level

        self.smallest_subtree = None

        def has_deepest_node(root: Optional[TreeNode]):
            if root is None:
                return False
            if root in deepest_nodes:
                if len(deepest_nodes) == 1:
                    self.smallest_subtree = root
                return True
            l, r = has_deepest_node(root.left), has_deepest_node(root.right)
            if l and r:
                self.smallest_subtree = root
            return l or r

        has_deepest_node(root)
        return self.smallest_subtree
