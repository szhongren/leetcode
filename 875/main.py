from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        brute force
        first, get sum of piles and / h
        rounded up, that's the min we need to search from
        for each potential val
        piles = [(pile // val) + 1 for pile in piles]
        return true if sum(piles) <= h
        """
        total_bananas = sum(piles)  # n
        left = ceil(total_bananas / h)
        right = max(piles)
        # times_to_eat = [ceil(pile / min_k) for pile in piles]
        # while sum(times_to_eat) > h:
        #     min_k += 1
        #     times_to_eat = [ceil(pile / min_k) for pile in piles]
        # return min_k
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)

            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1

        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right
