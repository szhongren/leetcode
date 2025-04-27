# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        approach
        if root == p:
        return root
        elif root == q:
        return root
        else if root.left has p and root.right has q or other way:
        return root
        else:
        return root.left or root.right
        """
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left, right = self.lowestCommonAncestor(
            root.left, p, q
        ), self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        else:
            return root
