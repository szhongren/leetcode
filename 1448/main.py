# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        recursive approach
        pass down max so far, so that each node can check if it's larger or equals max
        global counter for good nodes
        """
        self.counter = 0

        def goodNodesRecur(root: TreeNode, max_seen: int):
            if root is None:
                return
            if root.val >= max_seen:
                self.counter += 1
            new_max = max(max_seen, root.val)
            goodNodesRecur(root.left, new_max)
            goodNodesRecur(root.right, new_max)

        goodNodesRecur(root, root.val)
        return self.counter
