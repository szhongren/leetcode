"""
You need to find the largest value in each row of a binary tree.

Example:

Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if root != None:
            self.largestValuesRecur([root])
        return self.res

    def largestValuesRecur(self, row):
        next = []
        max = -10000000
        for node in row:
            if node.val > max:
                max = node.val
            if node.left != None:
                next.append(node.left)
            if node.right != None:
                next.append(node.right)
        self.res.append(max)
        if len(next) != 0:
            self.largestValuesRecur(next)
