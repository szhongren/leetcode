"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return levelOrderBottomRecur([root])

def levelOrderBottomRecur(queue):
    front = None
    new_queue = []
    while len(queue) != 0:
        curr = queue[0]
        queue = queue[1:]
        if curr == None:
            continue
        else:
            front = curr.val
            new_queue.append(curr.left)
            new_queue.append(curr.right)
    if front != None:
        return [front] + levelOrderBottomRecur(new_queue)
    else:
        return []

ans = Solution()
print(ans.rightSideView(make_tree([3, 9, 20, None, None, 15, 7])))
print(ans.rightSideView(make_tree([1, 2])))
print(ans.rightSideView(make_tree(
    [1,
    2, None,
    3, None, None, None,
    4, None, None, None, None, None, None, None,
    5])))
