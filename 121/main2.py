from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_lowest_price = prices[0]
        current_highest_price = prices[0]
        current_max_profit = 0
        for price in prices[1:]:
            if price < current_lowest_price:
                current_lowest_price = price
                current_highest_price = price
            if price > current_highest_price:
                current_highest_price = price
            profit = current_highest_price - current_lowest_price
            if profit > current_max_profit:
                current_max_profit = profit
        return current_max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
