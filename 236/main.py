"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                    for kid in (root.left, root.right))
        return root if left and right else left or right
        # def findNode(curr, node):
        #     if curr == None:
        #         return False
        #     if curr.val == node.val:
        #         return True
        #     return findNode(curr.left, node) or findNode(curr.right, node)
        # def LCARecur(curr, p, q):
        #     if curr in [None, p, q]:
        #         return curr
        #     p_in_left = findNode(curr.left, p)
        #     q_in_left = findNode(curr.left, q)
        #     p_in_right = findNode(curr.right, p)
        #     q_in_right = findNode(curr.right, q)
        #     if p_in_left and q_in_left:
        #         return LCARecur(curr.left, p, q)
        #     if p_in_right and q_in_right:
        #         return LCARecur(curr.right, p, q)
        #     return curr
        # return LCARecur(root, p, q)
        # what happens when you have duplicate nodes? your answer is undefined, can be the node itself or the node that is a parent of both of them

ans = Solution()
print(ans.lowestCommonAncestor(make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(1)).val)
print(ans.lowestCommonAncestor(make_tree([37, -34, -48, None, -100, -100, 48, None, None, None, None, None, None, -54, None, None, None, None, None, None, None, None, None, None, None, None, None, -71, -22]), TreeNode(-100), TreeNode(-71)).val)
print(ans.lowestCommonAncestor(None, TreeNode(5), TreeNode(1)).val)
