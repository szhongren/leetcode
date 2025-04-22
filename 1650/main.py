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
        take p, look to see if q is a parent or a child
        if parent, return q, if child, return p
        then, if neither, go to q and get parent until we find a node we have seen before
        """
        parent = p
        seen_parents = set()
        while parent is not None:
            if parent.val == q.val:
                return q
            seen_parents.add(parent.val)
            parent = parent.parent
        children = [p]
        # dfs
        while children:
            child = children.pop()
            if child.val == q.val:
                return p
            if child.left is not None:
                children.append(child.left)
            if child.right is not None:
                children.append(child.right)
        parent = q
        while parent is not None:
            if parent.val in seen_parents:
                return parent
            parent = parent.parent
        return None
