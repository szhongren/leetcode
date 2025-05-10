from typing import List
from functools import lru_cache


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        approach
        sort by start
        dp, for each potential trip, get the max dollars including this trip, or not including this trip

        """

        m = len(rides)
        rides.sort(key=lambda ride: ride[0])

        @lru_cache(None)
        def maxTaxiEarnings(i: int, last_trip_end: int):
            if i == m:
                return 0
            start, end, tip = rides[i][0], rides[i][1], rides[i][2]
            potential_paths = []
            if last_trip_end <= start:
                # take this trip
                potential_paths.append(end - start + tip + maxTaxiEarnings(i + 1, end))
            # skip this trip
            potential_paths.append(maxTaxiEarnings(i + 1, last_trip_end))
            return max(potential_paths)

        return maxTaxiEarnings(0, 0)


sol = Solution()
print(sol.maxTaxiEarnings(5, [[2, 5, 4], [1, 5, 1]]))
print(
    sol.maxTaxiEarnings(
        20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
    )
)
