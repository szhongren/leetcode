from typing import List
from collections import deque


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        approach:
        2 steps
        simulate gravity with a 2 pointer approach
        find first empty space (not #, not *), find #
        if *, find next empty space
        rotate
        """

        m = len(boxGrid)
        n = len(boxGrid[0])

        def rotate(box):
            result = []
            for j in range(n):
                row = []
                for i in range(m - 1, -1, -1):
                    row.append(box[i][j])
                result.append(row)
            return result

        def simulate_gravity(grid):
            for col_i in range(m):
                queue = deque()
                for row_i in range(n - 1, -1, -1):
                    cell = grid[row_i][col_i]
                    if cell == ".":
                        queue.append(row_i)
                    elif cell == "#":
                        if len(queue) == 0:
                            continue
                        lowest_row = queue.popleft()
                        grid[row_i][col_i], grid[lowest_row][col_i] = (
                            grid[lowest_row][col_i],
                            grid[row_i][col_i],
                        )
                        queue.append(row_i)
                    elif cell == "*":
                        queue = deque()
            return grid

        rotated_box = rotate(boxGrid)
        return simulate_gravity(rotated_box)


sol = Solution()
sol.rotateTheBox([["#", ".", "#"]])
sol.rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]])
