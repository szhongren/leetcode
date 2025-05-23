from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        approach
        check to make sure source and target are 0
        bfs with levels, if I am at the target, return level
        else, if bfs finished, return -1
        """
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        queue = deque([(0, 0)])
        grid[0][0] = 1
        path_len = 1
        while queue:
            new_queue = deque()
            for x, y in queue:
                if x == m - 1 and y == n - 1:
                    return path_len
                # 8 directions
                if x > 0 and y > 0 and grid[x - 1][y - 1] == 0:
                    grid[x - 1][y - 1] = 1
                    new_queue.append((x - 1, y - 1))

                if x > 0 and grid[x - 1][y] == 0:
                    grid[x - 1][y] = 1
                    new_queue.append((x - 1, y))

                if x > 0 and y < n - 1 and grid[x - 1][y + 1] == 0:
                    grid[x - 1][y + 1] = 1
                    new_queue.append((x - 1, y + 1))

                if y < n - 1 and grid[x][y + 1] == 0:
                    grid[x][y + 1] = 1
                    new_queue.append((x, y + 1))

                if x < m - 1 and y < n - 1 and grid[x + 1][y + 1] == 0:
                    grid[x + 1][y + 1] = 1
                    new_queue.append((x + 1, y + 1))

                if x < m - 1 and grid[x + 1][y] == 0:
                    grid[x + 1][y] = 1
                    new_queue.append((x + 1, y))

                if x < m - 1 and y > 0 and grid[x + 1][y - 1] == 0:
                    grid[x + 1][y - 1] = 1
                    new_queue.append((x + 1, y - 1))

                if y > 0 and grid[x][y - 1] == 0:
                    grid[x][y - 1] = 1
                    new_queue.append((x, y - 1))

            path_len += 1
            queue = new_queue
        return -1
