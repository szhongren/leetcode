"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

     3
    / \
   2   3
    \   \
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9.
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
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def transformTree(node):
            if node == None:
                return TreeNode([0, 0])
            node.left = transformTree(node.left)
            node.right = transformTree(node.right)
            curr_val = node.val
            node.val = [None, None]
            rob = 0
            notrob = 1
            node.val[notrob] = node.left.val[rob] + node.right.val[rob]
            node.val[rob] = max(node.val[notrob], curr_val + node.left.val[notrob] + node.right.val[notrob])
            return node
            # only works when space between houses robbed can only be 1
        return max(transformTree(root).val)

ans = Solution()
print(ans.rob(make_tree([3, 2, 3, None, 3, None, 1])))
print(ans.rob(make_tree([3, 4, 5, 1, 3, None, 1])))
print(ans.rob(make_tree([])))
