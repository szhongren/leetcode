from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        approach
        bfs: takes x and y, and sets 1 to 0
        don't need to track visited like this
        for cell in grid:
            if == 1:
                bfs
                count += 1
        return count
        """
        num_islands = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue = deque([(i, j)])
                    grid[i][j] = "0"
                    while queue:
                        a, b = queue.popleft()
                        if a > 0 and grid[a - 1][b] == "1":
                            grid[a - 1][b] = "0"
                            queue.append((a - 1, b))
                        if b > 0 and grid[a][b - 1] == "1":
                            grid[a][b - 1] = "0"
                            queue.append((a, b - 1))
                        if a < m - 1 and grid[a + 1][b] == "1":
                            grid[a + 1][b] = "0"
                            queue.append((a + 1, b))
                        if b < n - 1 and grid[a][b + 1] == "1":
                            grid[a][b + 1] = "0"
                            queue.append((a, b + 1))
                    num_islands += 1
        return num_islands
