from typing import Optional
from heapq import heappush, heappop

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: "Node") -> int:
        """
        approach
        recursive
        2 cases
        diameter goes through the root
        diameter is fully is left or right subtree
        thus, each recursive call should return (diameter, max_height)
        each node, should return max(left_height + right_height, diameter_right, diameter_left)
        state: root | rleft | rright | left_dia | right_dia | left_h | right_h
               1      2       3
        """
        if root is None:
            return 0

        def diameterRecur(root: Optional["Node"]):
            if root is None:
                return (0, -1)
            heap = []
            max_diameter = 0
            for child in root.children:
                diameter, height = diameterRecur(child)
                if diameter > max_diameter:
                    max_diameter = diameter
                heappush(heap, -height)
            if len(heap) == 0:
                return (0, 0)
            if len(heap) == 1:
                height = (-heap[0]) + 1
                return (max(max_diameter, height), height)

            h1, h2 = -heappop(heap), -heappop(heap)
            diameter_through_root = h1 + h2 + 2
            return (
                max(max_diameter, diameter_through_root),
                max(h1, h2) + 1,
            )

        return diameterRecur(root)[0]
