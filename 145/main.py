"""
Given a binary tree, return the postorder traversal of its nodes' values.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk_a = []
        stk_b = []
        stk_a.append(root)
        while len(stk_a) != 0:
            curr = stk_a[-1]
            stk_a = stk_a[:-1]
            if curr == None:
                continue
            stk_b.append(curr.val)
            stk_a.append(curr.left)
            stk_a.append(curr.right)

        return stk_b.reverse()

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
print(ans.postorderTraversal(tree))
