"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        """
        approach
        look for parents of p, up till the root node
        put each visited parent in seen nodes
        if q visited, return q
        else, look for parents of q, until we see a node we have seen before
        return that node
        edge cases:
        * nodes in tree?
        both nodes are the same? still works
        if p is parent of q or q is parent of p, still works
        """
        seen_nodes = set()
        curr_node = p
        while curr_node is not None:
            if curr_node.val == q.val:
                return curr_node
            seen_nodes.add(curr_node.val)
            curr_node = curr_node.parent
        # q not parent of p
        curr_node = q
        while curr_node is not None:
            if curr_node.val in seen_nodes:
                return curr_node
            seen_nodes.add(curr_node.val)
            curr_node = curr_node.parent
        return None
