"""
Find the sum of all left leaves in a given binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return sumLeftLeavesHelper(root, False)

def sumLeftLeavesHelper(root, left):
    if root == None:
        return 0
    elif root.left == None and root.right == None and left:
        return root.val
    else:
        return sumLeftLeavesHelper(root.left, True) + sumLeftLeavesHelper(root.right, False)
