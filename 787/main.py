from typing import List
from math import inf


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        approach
        use bellman ford
        """
        prices = [inf for _ in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for a, b, cost in flights:
                if prices[a] + cost < temp[b]:
                    temp[b] = prices[a] + cost
            prices = temp

        return prices[dst] if prices[dst] != inf else -1
