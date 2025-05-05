from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        while level:
        result.append(avg)

        edge cases
        None
        """
        if root is None:
            return []
        result = []
        nodes = [root]
        while nodes:
            result.append(sum([n.val for n in nodes]) / len(nodes))
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return result
