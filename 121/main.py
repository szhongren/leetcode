from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        approach
        iterate through prices
        find smallest value so far, and check to see if current price would result in a larger total profit
        return at the end
        """
        max_profit = 0
        lowest_price = inf
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            if price - lowest_price > max_profit:
                max_profit = price - lowest_price
        return max_profit
