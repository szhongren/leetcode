from typing import List
from collections import deque
from pprint import pprint


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        approach
        bfs for the ones on the side, and edit the grid to change to zeros
        then, for remaining, bfs, each bfs iteration count += 1
        return count
        """
        m, n = len(grid), len(grid[0])

        # step 1
        def bfs(x: int, y: int):
            queue = deque()
            queue.append((x, y))
            total = 0
            while queue:
                i, j = queue.popleft()
                if not i == 0:
                    # bottom
                    if grid[i - 1][j] == 1:
                        queue.append((i - 1, j))
                if not j == 0:
                    # right
                    if grid[i][j - 1] == 1:
                        queue.append((i, j - 1))
                if not i == m - 1:
                    # top
                    if grid[i + 1][j] == 1:
                        queue.append((i + 1, j))
                if not j == n - 1:
                    # left
                    if grid[i][j + 1] == 1:
                        queue.append((i, j + 1))
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                total += 1
            return total

        for j in range(n):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[m - 1][j] == 1:
                bfs(m - 1, j)

        for i in range(m):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][n - 1] == 1:
                bfs(i, n - 1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += bfs(i, j)
        return count


sol = Solution()
# sol.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
# sol.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
# sol.numEnclaves(
#     [
#         [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#         [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
#         [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#         [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
#         [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
#         [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
#         [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
#         [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
#         [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
#     ]
# )

print(
    sol.numEnclaves(
        [
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
        ]
    )
)
