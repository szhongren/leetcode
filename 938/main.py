# Definition for a binary tree node.
class TreeNode:
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

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0
        left_sum = self.rangeSumBST(root.left, L, R)
        right_sum = self.rangeSumBST(root.right, L, R)
        curr_val = 0
        if root.val <= R and root.val >= L:
            curr_val = root.val
        return curr_val + left_sum + right_sum


tree = make_tree([10, 5, 15, 3, 7, None, 18])
ans = Solution()
print(ans.rangeSumBST(tree, 7, 15))
