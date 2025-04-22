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
        give each node a vertical order, and a horizontal order, and put in a map of maps
        then, sort the map and output a list of lists
        """

        ordered_nodes = {}

        def verticalOrderRecur(root: Optional[TreeNode], v: int, h: int):
            if root is None:
                return
            if v not in ordered_nodes:
                ordered_nodes[v] = {}
            if h not in ordered_nodes[v]:
                ordered_nodes[v][h] = []
            ordered_nodes[v][h].append(root.val)
            verticalOrderRecur(root.left, v - 1, h + 1)
            verticalOrderRecur(root.right, v + 1, h + 1)

        verticalOrderRecur(root, 0, 0)
        ordered_v = sorted(ordered_nodes.keys())
        result = []
        for v in ordered_v:
            sub_result = []
            ordered_h = sorted(ordered_nodes[v].keys())
            for h in ordered_h:
                sub_result += ordered_nodes[v][h]
            result.append(sub_result)
        return result
