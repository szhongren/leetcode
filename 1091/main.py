from collections import deque
from typing import List, Tuple


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        approach
        bfs from source
        """

        seen = {(0, 0): 1}
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        def generate_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
            potentials = [
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
            ]
            return [
                (a, b)
                for a, b in potentials
                if a >= 0
                and a < len(grid)
                and b >= 0
                and b < len(grid[0])
                and grid[a][b] != 1
            ]

        queue = deque()
        queue.extend(generate_neighbors(0, 0))
        while len(queue) != 0:
            a, b = queue.popleft()
            neighbors = generate_neighbors(a, b)
            potential_scores = [seen[(x, y)] for x, y in neighbors if (x, y) in seen]
            queue.extend([(x, y) for x, y in neighbors if (x, y) not in seen])
            seen[(a, b)] = min(potential_scores) + 1
        return seen.get((len(grid) - 1, len(grid[0]) - 1), -1)


sol = Solution()
# print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(
    sol.shortestPathBinaryMatrix(
        [
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
        ]
    )
)
