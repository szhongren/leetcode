from typing import List
from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        approach
        bfs/dfs
        for each 0 we see, bfs
        if we get to the end of the bfs without hitting an edge, +1 island
        else, continue, mark this iteration as not an island, and move on to the next grid cell
        we can set the 0s to 1s as a shortcut, this way we don't have to keep track of visited cells separately
        """
        m = len(grid)
        n = len(grid[0])

        def bfs(x: int, y: int):
            is_island = True
            queue = deque([(x, y)])
            while queue:
                a, b = queue.popleft()
                grid[a][b] = 1
                if a == 0 or b == 0 or a == m - 1 or b == n - 1:
                    is_island = False
                if a > 0 and grid[a - 1][b] == 0:
                    queue.append((a - 1, b))
                if b > 0 and grid[a][b - 1] == 0:
                    queue.append((a, b - 1))
                if a < m - 1 and grid[a + 1][b] == 0:
                    queue.append((a + 1, b))
                if b < n - 1 and grid[a][b + 1] == 0:
                    queue.append((a, b + 1))
            return is_island

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if bfs(i, j):
                        num_islands += 1
        return num_islands
