from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        approach
        dp
        from top to bottom
        dp[i][j] += min(dp[i - 1][j - 1], dp[i- 1][j], dp[i-1][j + 1])
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        for i in range(1, n):
            for j in range(n):
                sources = [matrix[i - 1][j]]
                if j > 0:
                    sources.append(matrix[i - 1][j - 1])
                if j < n - 1:
                    sources.append(matrix[i - 1][j + 1])
                matrix[i][j] += min(sources)
        return min(matrix[n - 1])
