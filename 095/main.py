"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level = 0):
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


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTreesRecur(1, n)

    def genTreesRecur(self, start, end):
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(start)]
        res = []
        for i in range(start, end + 1):
            l = self.genTreesRecur(start, i - 1)
            r = self.genTreesRecur(i + 1, end)
            for x in range(len(l)):
                for y in range(len(r)):
                    tmp = TreeNode(i)
                    tmp.left = l[x]
                    tmp.right = r[y]
                    res.append(tmp)
        return res

ans = Solution()
for tr in ans.generateTrees(3):
    print(tr)
