from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    # Mark current cell before BFS
                    grid[i][j] = "0"
                    queue = deque([(i, j)])

                    while queue:
                        x, y = queue.popleft()
                        # Check all 4 directions inline
                        if x > 0 and grid[x - 1][y] == "1":
                            grid[x - 1][y] = "0"
                            queue.append((x - 1, y))
                        if x < rows - 1 and grid[x + 1][y] == "1":
                            grid[x + 1][y] = "0"
                            queue.append((x + 1, y))
                        if y > 0 and grid[x][y - 1] == "1":
                            grid[x][y - 1] = "0"
                            queue.append((x, y - 1))
                        if y < cols - 1 and grid[x][y + 1] == "1":
                            grid[x][y + 1] = "0"
                            queue.append((x, y + 1))

        return count


sol = Solution()
print(
    sol.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
