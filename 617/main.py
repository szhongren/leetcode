"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
    Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
         3
        / \
       4   5
      / \   \
     5   4   7

Note: The merging process must start from the root nodes of both trees.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = repr(self.val) + '\n'
        if level != 0:
            ret = "-" * (level - 1) + '>' + ret
        if self.left != None:
            ret += self.left.__str__(level + 1)
        if self.right != None:
            ret += self.right.__str__(level + 1)
        return ret


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


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def mergeTreesRecur(t1, t2):
            if t1 is None and t2 is None:
                return None
            newNode = TreeNode(0)
            if t1 is None:
                newNode.val = t2.val
                newNode.left = mergeTreesRecur(None, t2.left)
                newNode.right = mergeTreesRecur(None, t2.right)
            elif t2 is None:
                newNode.val = t1.val
                newNode.left = mergeTreesRecur(t1.left, None)
                newNode.right = mergeTreesRecur(t1.right, None)
            else:
                newNode.val = t1.val + t2.val
                newNode.left = mergeTreesRecur(t1.left, t2.left)
                newNode.right = mergeTreesRecur(t1.right, t2.right)
            return newNode
        return mergeTreesRecur(t1, t2)


ans = Solution()
tree1 = make_tree([1, 3, 2, 5])
tree2 = make_tree([2, 1, 3, None, 4, None, 7])
print(ans.mergeTrees(tree1, tree2))
