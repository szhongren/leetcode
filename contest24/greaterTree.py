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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        def sumTree(node):
            if node == None:
                return 0
            return node.val + sumTree(node.right) + sumTree(node.left)
        def convertBSTRecur(node, extra):
            if node == None:
                return None
            right_sum = sumTree(node.right)
            node.right = convertBSTRecur(node.right, extra)
            node.val += right_sum + extra
            node.left = convertBSTRecur(node.left, node.val)
            return node
        return convertBSTRecur(root, 0)

ans = Solution()
test = ans.convertBST(make_tree([5, 2, 13]))

print("test")
