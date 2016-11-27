"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.zigzagLevelOrderRecur([root], True)

    def zigzagLevelOrderRecur(self, queue, forward):
        curr_level = []
        new_queue = []
        while len(queue) != 0:
            curr = queue[0]
            queue = queue[1:]
            if curr == None:
                continue
            else:
                curr_level.append(curr.val)
                if forward:
                    new_queue.append(curr.left)
                new_queue.append(curr.right)
                if not forward:
                    new_queue.append(curr.left)
        if len(new_queue) != 0:
            return [curr_level] + self.zigzagLevelOrderRecur(list(reversed(new_queue)), not forward)
        else:
            return []

ans = Solution()
print(ans.zigzagLevelOrder(make_tree([3, 9, 20, None, None, 15, 7])))