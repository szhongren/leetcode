"""
Invert a binary tree.
"""

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            new_left = self.invertTree(root.right)
            new_right = self.invertTree(root.left)
            root.right = new_right
            root.left = new_left
            return root