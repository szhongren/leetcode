from typing import List
from collections import deque
from math import inf
from pprint import pprint


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        approach
        use bfs on first island
        set values to -1
        use bfs on second island
        set values to -2
        from every -1, bfs
        """
        m = len(grid)
        n = len(grid[0])

        def bfs_island(x: int, y: int, value: int):
            queue = deque([(x, y)])
            seen = set()
            while queue:
                a, b = queue.popleft()
                if (a, b) in seen:
                    continue
                seen.add((a, b))
                grid[a][b] = value
                if a > 0 and grid[a - 1][b] == 1:
                    queue.append((a - 1, b))
                if a < m - 1 and grid[a + 1][b] == 1:
                    queue.append((a + 1, b))
                if b > 0 and grid[a][b - 1] == 1:
                    queue.append((a, b - 1))
                if b < n - 1 and grid[a][b + 1] == 1:
                    queue.append((a, b + 1))

        def bfs_water(x: int, y: int, search: int):
            queue = deque([(x, y)])
            seen = set()
            level = 1
            while queue:
                new_queue = deque()
                while queue:
                    a, b = queue.popleft()
                    if grid[a][b] == search:
                        return level
                    if (a, b) in seen:
                        continue
                    seen.add((a, b))
                    if a > 0 and grid[a - 1][b] in (0, search):
                        new_queue.append((a - 1, b))
                    if a < m - 1 and grid[a + 1][b] in (0, search):
                        new_queue.append((a + 1, b))
                    if b > 0 and grid[a][b - 1] in (0, search):
                        new_queue.append((a, b - 1))
                    if b < n - 1 and grid[a][b + 1] in (0, search):
                        new_queue.append((a, b + 1))
                level += 1
                queue = new_queue
            return None

        seen_first_island = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if seen_first_island:
                        bfs_island(i, j, -1)
                    else:
                        bfs_island(i, j, -2)
                    seen_first_island = not seen_first_island
        min_dist = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    maybe_distance = bfs_water(i, j, -2)
                    if maybe_distance is None:
                        continue
                    min_dist = min(min_dist, maybe_distance)
        return min_dist - 2


sol = Solution()
print(sol.shortestBridge([[0, 1], [1, 0]]))
print(sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(
    sol.shortestBridge(
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
    )
)

print(
    sol.shortestBridge(
        [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
