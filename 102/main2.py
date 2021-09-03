from typing import List, Optional


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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use extra value to keep track of level so I can separate after
        queue = [(root, 0)]
        levels = {}
        while len(queue) != 0:
            # pop first item off
            current_node, level = queue[0]
            queue = queue[1:]
            # if this is None, just go to next item because we don't have to do anything
            if current_node is None:
                continue
            # otherwise, first we check to see if level has an entry in levels
            if level not in levels:
                levels[level] = []
            # guaranteed to have an entry for levels here
            levels[level].append(current_node.val)
            queue.append((current_node.left, level + 1))
            queue.append((current_node.right, level + 1))
        return [levels[i] for i in sorted(levels.keys())]


"""
1
2, 3
4, 5, 6, 7
"""

ans = Solution()
print(ans.levelOrder(make_tree([3, 9, 20, None, None, 15, 7])))
print(ans.levelOrder(make_tree([1, 2])))
print(
    ans.levelOrder(
        make_tree(
            [
                1,
                2,
                None,
                3,
                None,
                None,
                None,
                4,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                5,
            ]
        )
    )
)
