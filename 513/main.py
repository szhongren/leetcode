"""
 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findBottomLeftValueRecur([root])

    def findBottomLeftValueRecur(self, row):
        next = []
        for node in row:
            if node.left != None:
                next.append(node.left)
            if node.right != None:
                next.append(node.right)
        if len(next) == 0:
            return row[0].val
        else:
            return self.findBottomLeftValueRecur(next)

ans = Solution()
