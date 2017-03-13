"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.found = {}
        self.max_count = 0
        self.modes = []
        self.findModeRecur(root)
        return self.modes

    def findModeRecur(self, root):
        if root == None:
            return
        curr = root.val
        if curr in self.found:
            self.found[curr] += 1
        else:
            self.found[curr] = 1
        if self.found[curr] == self.max_count:
            self.modes.append(curr)
        elif self.found[curr] > self.max_count:
            self.max_count = self.found[curr]
            self.modes = [curr]
        self.findModeRecur(root.left)
        self.findModeRecur(root.right)


ans = Solution()
print(ans.findMode(make_tree([1, None, 2, None, None, 2])))
print(ans.findMode(make_tree([1, None, 2])))
