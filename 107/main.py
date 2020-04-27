"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        return levelOrderBottomRecur(queue)

def levelOrderBottomRecur(queue):
    curr_level = []
    new_queue = []
    while len(queue) != 0:
        curr = queue[0]
        queue = queue[1:]
        if curr == None:
            continue
        else:
            curr_level.append(curr.val)
            new_queue.append(curr.left)
            new_queue.append(curr.right)
    if len(new_queue) != 0:
        return levelOrderBottomRecur(new_queue) + [curr_level]
    else:
        return []


ans = Solution()
print(ans.levelOrderBottom(make_tree([3, 9, 20, None, None, 15, 7])))
print(ans.levelOrderBottom(make_tree([1, 2])))
print(ans.levelOrderBottom(make_tree(
    [1,
    2, None,
    3, None, None, None,
    4, None, None, None, None, None, None, None,
    5])))