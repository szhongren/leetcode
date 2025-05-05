from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder first item is root
        look in inorder, left of root is left subtree
        look in inorder, right of root is left subtree
        recurse
        """
        if len(preorder) == 0:
            return None

        def buildTree(preorder: List[int], inorder: List[int]):
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root = TreeNode(preorder[0])
            root_i = inorder.index(root.val)
            root.left = buildTree(preorder[1 : root_i + 1], inorder[:root_i])
            root.right = buildTree(preorder[root_i + 1 :], inorder[root_i + 1 :])
            return root

        return buildTree(preorder, inorder)
