"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.pathSumRecur(root, sum, [])
        return self.res

    def pathSumRecur(self, root, sum, path):
        """
        :type root: TreeNode
        :type sum: int
        :type path: List[int]
        :rtype: void
        """
        if root == None:
            return
        else:
            if root.left == None and root.right == None and root.val == sum:
                self.res.append(path + [root.val])
            else:
                sum -= root.val
                self.pathSumRecur(root.left, sum, path + [root.val])
                self.pathSumRecur(root.right, sum, path + [root.val])

ans = Solution()
print(ans.pathSum(make_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]), 22))