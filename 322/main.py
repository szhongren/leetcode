"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # if amount == 0:
        #     return 0

        # dp = [-1 for i in range(amount + 1)]
        # for i in range(len(dp)):
        #     if i in coins:
        #         dp[i] = 1
        #     else:
        #         for c in coins:
        #             if i - c >= 0:
        #                 if dp[i - c] == -1:
        #                     pass
        #                 elif dp[i] == -1:
        #                     dp[i] = dp[i - c] + 1
        #                 else:
        #                     dp[i] = min(dp[i], dp[i - c] + 1)
        # return dp[-1]
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

ans = Solution()
print(ans.coinChange([496,154,300,357,327,248,201,341,145,248,316], 6776))
print(ans.coinChange([2], 3))
print(ans.coinChange([1, 2, 5], 11))
