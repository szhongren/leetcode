"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                elif j == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = 0
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    else:
                        dp[i][j] = 0
        return dp[-1][-1]


ans = Solution()
print(ans.uniquePathsWithObstacles(
    [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
))