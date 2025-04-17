from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def canReachDestination(maxDiff: int) -> bool:
            ROWS, COLS = len(heights), len(heights[0])
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                x, y = stack.pop()
                if x == ROWS - 1 and y == COLS - 1:
                    return True

                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (
                        0 <= nx < ROWS
                        and 0 <= ny < COLS
                        and (nx, ny) not in seen
                        and abs(heights[nx][ny] - heights[x][y]) <= maxDiff
                    ):
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            return False

        left, right = 0, 10**6
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
print(sol.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(sol.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(
    sol.minimumEffortPath(
        [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
    )
)
print(
    sol.minimumEffortPath(
        [
            [8, 3, 2, 5, 2, 10, 7, 1, 8, 9],
            [1, 4, 9, 1, 10, 2, 4, 10, 3, 5],
            [4, 10, 10, 3, 6, 1, 3, 9, 8, 8],
            [4, 4, 6, 10, 10, 10, 2, 10, 8, 8],
            [9, 10, 2, 4, 1, 2, 2, 6, 5, 7],
            [2, 9, 2, 6, 1, 4, 7, 6, 10, 9],
            [8, 8, 2, 10, 8, 2, 3, 9, 5, 3],
            [2, 10, 9, 3, 5, 1, 7, 4, 5, 6],
            [2, 3, 9, 2, 5, 10, 2, 7, 1, 8],
            [9, 10, 4, 10, 7, 4, 9, 3, 1, 6],
        ]
    )
)
