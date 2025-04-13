from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        """
        * do recursion, until we only have 1 item
        * then set leaf and value
        * for each level, if all 4 are leaves and have same value, set children to None, and set this as leaf
        """
        if len(grid) == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        size = len(grid)
        tl, tr, bl, br = (
            self.construct([row[: size // 2] for row in grid[: size // 2]]),
            self.construct([row[size // 2 :] for row in grid[: size // 2]]),
            self.construct([row[: size // 2] for row in grid[size // 2 :]]),
            self.construct([row[size // 2 :] for row in grid[size // 2 :]]),
        )
        check = tl.val
        if (
            all([tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf])
            and tr.val == check
            and bl.val == check
            and br.val == check
        ):
            return Node(check, True, None, None, None, None)
        return Node(check, False, tl, tr, bl, br)


sol = Solution()
print(sol.construct([[0, 1], [1, 0]]))
