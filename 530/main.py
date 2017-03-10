"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(ls):
    """
    :type ls: List[int]
    :rtype: TreeNode
    """
    if len(ls) == 0:
        return None
    list_nodes = list(map(lambda x: TreeNode(x) if x != None else None, ls))
    length = len(list_nodes)
    for i in range(length // 2):
        if list_nodes[i] != None:
            if i * 2 + 1 < length:
                list_nodes[i].left = list_nodes[i * 2 + 1]
            if i * 2 + 2 < length:
                list_nodes[i].right = list_nodes[i * 2 + 2]
    return list_nodes[0]

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.min = 1000000000
        # self.getMinimumDifferenceRecur(root)
        # return self.min
        self.in_order = []
        self.getMinimumDifferenceInOrderTraversal(root)
        return self.mindiff(self.in_order)

    # def getMinimumDifferenceRecur(self, root):
    #     if root.left == None and root.right == None:
    #         return 100000000
    #     if root.left != None:
    #         self.min = min(self.min, root.val - max_tree(root.left))
    #         self.min = min(self.min, self.getMinimumDifferenceRecur(root.left))
    #     if root.right != None:
    #         self.min = min(self.min, min_tree(root.right) - root.val)
    #         self.min = min(self.min, self.getMinimumDifferenceRecur(root.right))
    #     return self.min

    def getMinimumDifferenceInOrderTraversal(self, root):
        if root == None:
            return
        self.getMinimumDifferenceInOrderTraversal(root.left)
        self.in_order.append(root.val)
        self.getMinimumDifferenceInOrderTraversal(root.right)

    def mindiff(self, in_order):
        min_diff = 1000000000
        for i in range(len(in_order) - 1):
            min_diff = min(min_diff, in_order[i + 1] - in_order[i])
        return min_diff


def max_tree(node):
    while node.right != None:
        node = node.right
    return node.val

def min_tree(node):
    while node.left != None:
        node = node.left
    return node.val

ans = Solution()
print(ans.getMinimumDifference(make_tree([1, None, 2])))
