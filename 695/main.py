from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        approach
        for cell in grid
        if cell == 1:
        bfs
        keep track of number of cells visited
        when we do bfs, set grid[i][j] to 0
        every time we see a new cell, check the max size of the island
        return max_island_size
        """
        self.max_island_size = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(x: int, y: int):
            size = 0
            queue = deque([(x, y)])
            grid[x][y] = 0
            while queue:
                a, b = queue.popleft()
                size += 1
                if a > 0 and grid[a - 1][b] == 1:
                    grid[a - 1][b] = 0
                    queue.append((a - 1, b))
                if a < m - 1 and grid[a + 1][b] == 1:
                    grid[a + 1][b] = 0
                    queue.append((a + 1, b))
                if b > 0 and grid[a][b - 1] == 1:
                    grid[a][b - 1] = 0
                    queue.append((a, b - 1))
                if b < n - 1 and grid[a][b + 1] == 1:
                    grid[a][b + 1] = 0
                    queue.append((a, b + 1))
            self.max_island_size = max(self.max_island_size, size)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        return self.max_island_size
