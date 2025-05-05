from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        approach
        iterate through the tree, append each node to a list as a value of a map from vertical i to nodes
        inherently top to bottom, left to right if I do root, left, right
        iterate through the keys and append to list
        """
        nodes_map = {}

        def verticalTraversalRecur(root: Optional[TreeNode], i: int, j: int):
            if root is None:
                return
            if (i, j) not in nodes_map:
                nodes_map[(i, j)] = []
            nodes_map[(i, j)].append(root.val)
            verticalTraversalRecur(root.left, i - 1, j + 1)
            verticalTraversalRecur(root.right, i + 1, j + 1)

        verticalTraversalRecur(root, 0, 0)
        keys_to_check = sorted(nodes_map.keys())
        temp_map = {}
        for x, y in keys_to_check:
            if x not in temp_map:
                temp_map[x] = []
            temp_map[x] += sorted(nodes_map[(x, y)])
        keys_to_check = sorted(temp_map.keys())
        result = []
        for k in keys_to_check:
            result.append(temp_map[k])
        return result
