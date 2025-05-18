from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        approach
        map of (v, h) to list
        - change of mind, map[v][h] instead
        - because we want to concat items in same v
        recursive call, left, node, right
        after, sort keys by v, then h
        """

        order = {}

        def verticalOrderRecur(root: Optional[TreeNode], v: int, h: int):
            if root is None:
                return
            if v not in order:
                order[v] = {}
            if h not in order[v]:
                order[v][h] = []

            verticalOrderRecur(root.left, v - 1, h + 1)
            order[v][h].append(root.val)
            verticalOrderRecur(root.right, v + 1, h + 1)

        verticalOrderRecur(root, 0, 0)

        result = []
        for v in sorted(order.keys()):
            vertical_result = []
            for h in sorted(order[v].keys()):
                vertical_result += order[v][h]
            result.append(vertical_result)
        return result
