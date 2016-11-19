"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val or root.val == q.val or (p.val < root.val and root.val < q.val) or (q.val < root.val and root.val < p.val):
            return root
        else:
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)


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

ans = Solution()
tree = make_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
print(ans.lowestCommonAncestor(tree, TreeNode(2), TreeNode(8)).val)
print(ans.lowestCommonAncestor(tree, TreeNode(2), TreeNode(4)).val)