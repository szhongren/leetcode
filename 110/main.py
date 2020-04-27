"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

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

def treeMinHeight(tr):
    """
    :type tr: TreeNode
    :rtype: int
    """
    if tr == None:
        return 0
    else:
        return 1 + min(treeMinHeight(tr.left), treeMinHeight(tr.right))


def treeMaxHeight(tr):
    """
    :type tr: TreeNode
    :rtype: int
    """
    if tr == None:
        return 0
    else:
        return 1 + max(treeMaxHeight(tr.left), treeMaxHeight(tr.right))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif abs(treeMaxHeight(root.left) - treeMaxHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

ans = Solution()
print(ans.isBalanced(make_tree([1, 2, 2, 3, 3, 3, 3, 4, 4])))
tree = make_tree([3, 1, None, None, 2])
print(treeMaxHeight(tree))
print(treeMinHeight(tree))
print(ans.isBalanced(tree))
