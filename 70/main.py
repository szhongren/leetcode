class Solution:
    def climbStairs(self, n: int) -> int:
        """
        approach
        dp
        for every step, we have previous step + 2 steps ago added together
        prepend with 0
        1 1 2 3 5
          1 2 3
        fibonacci
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
