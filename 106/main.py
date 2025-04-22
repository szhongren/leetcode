from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        approach:
        last of postorder is root
        with that, we can find left and right subtrees
        recur
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)
        root = postorder[-1]
        root_i = inorder.index(root)
        left_inorder = inorder[:root_i]
        right_inorder = inorder[root_i + 1 :]
        left_postorder = postorder[:root_i]
        right_postorder = postorder[root_i:-1]
        left_subtree = self.buildTree(left_inorder, left_postorder)
        right_subtree = self.buildTree(right_inorder, right_postorder)
        return TreeNode(root, left_subtree, right_subtree)
