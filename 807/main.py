class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [0 for _ in grid]
        col_maxes = [0 for _ in grid[0]]
        result = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                row_maxes[i] = max(row_maxes[i], value)
                col_maxes[j] = max(col_maxes[j], value)
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                result += min(row_maxes[i], col_maxes[j]) - value
        return result

ans = Solution()
print(ans.maxIncreaseKeepingSkyline([
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0],
]))
