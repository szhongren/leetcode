from typing import Dict

from functools import cache


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        for i, j in x, y:
            visited[(i, j)] = False

        call helper

        def dfs(visited):
            take any one that's not been visited
            visit connected points
            log max
            if all visited
            return max
        """
        max_size = 0
        visited = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited[(i, j)] = False
        not_visited = [a for a in visited]

        @cache
        def dfs(x, y):
            if (x, y) not in visited:
                return 0
            if visited[(x, y)]:
                return 0
            a, b, c, d = (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
            visited[(x, y)] = True
            return grid[x][y] + dfs(*a) + dfs(*b) + dfs(*c) + dfs(*d)

        for x, y in not_visited:
            if visited[(x, y)]:
                continue
            max_size = max(dfs(x, y), max_size)
        return max_size


sol = Solution()
print(
    sol.maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
